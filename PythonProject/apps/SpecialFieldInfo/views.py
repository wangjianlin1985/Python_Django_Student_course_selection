from django.views.generic import View
from apps.BaseView import BaseView
from django.shortcuts import render
from django.core.paginator import Paginator
from apps.SpecialFieldInfo.models import SpecialFieldInfo
from apps.CollegeInfo.models import CollegeInfo
from django.http import JsonResponse
from django.http import FileResponse
from apps.BaseView import ImageFormatException
from django.conf import settings
import pandas as pd
import os


class FrontAddView(BaseView):  # 前台专业信息添加
    def primaryKeyExist(self, specialFieldNumber):  # 判断主键是否存在
        try:
            SpecialFieldInfo.objects.get(specialFieldNumber=specialFieldNumber)
            return True
        except SpecialFieldInfo.DoesNotExist:
            return False

    def get(self,request):
        collegeInfos = CollegeInfo.objects.all()  # 获取所有学院信息
        context = {
            'collegeInfos': collegeInfos,
        }

        # 使用模板
        return render(request, 'SpecialFieldInfo/specialFieldInfo_frontAdd.html', context)

    def post(self, request):
        specialFieldNumber = request.POST.get('specialFieldInfo.specialFieldNumber') # 判断专业编号是否存在
        if self.primaryKeyExist(specialFieldNumber):
            return JsonResponse({'success': False, 'message': '专业编号已经存在'})

        specialFieldInfo = SpecialFieldInfo() # 新建一个专业信息对象然后获取参数
        specialFieldInfo.specialFieldNumber = specialFieldNumber
        specialFieldInfo.specialFieldName = request.POST.get('specialFieldInfo.specialFieldName')
        specialFieldInfo.specialCollegeNumber = CollegeInfo.objects.get(collegeNumber=request.POST.get('specialFieldInfo.specialCollegeNumber.collegeNumber'))
        specialFieldInfo.specialBirthDate = request.POST.get('specialFieldInfo.specialBirthDate')
        specialFieldInfo.specialMan = request.POST.get('specialFieldInfo.specialMan')
        specialFieldInfo.specialTelephone = request.POST.get('specialFieldInfo.specialTelephone')
        specialFieldInfo.specialMemo = request.POST.get('specialFieldInfo.specialMemo')
        specialFieldInfo.save() # 保存专业信息信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class FrontModifyView(BaseView):  # 前台修改专业信息
    def get(self, request, specialFieldNumber):
        context = {'specialFieldNumber': specialFieldNumber}
        return render(request, 'SpecialFieldInfo/specialFieldInfo_frontModify.html', context)


class FrontListView(BaseView):  # 前台专业信息查询列表
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        self.getCurrentPage(request)  # 获取当前要显示第几页
        # 下面获取查询参数
        specialFieldNumber = self.getStrParam(request, 'specialFieldNumber')
        specialFieldName = self.getStrParam(request, 'specialFieldName')
        specialCollegeNumber_collegeNumber = self.getStrParam(request, 'specialCollegeNumber.collegeNumber')
        specialBirthDate = self.getStrParam(request, 'specialBirthDate')
        # 然后条件组合查询过滤
        specialFieldInfos = SpecialFieldInfo.objects.all()
        if specialFieldNumber != '':
            specialFieldInfos = specialFieldInfos.filter(specialFieldNumber__contains=specialFieldNumber)
        if specialFieldName != '':
            specialFieldInfos = specialFieldInfos.filter(specialFieldName__contains=specialFieldName)
        if specialCollegeNumber_collegeNumber != '':
            specialFieldInfos = specialFieldInfos.filter(specialCollegeNumber=specialCollegeNumber_collegeNumber)
        if specialBirthDate != '':
            specialFieldInfos = specialFieldInfos.filter(specialBirthDate__contains=specialBirthDate)
        # 对查询结果利用Paginator进行分页
        self.paginator = Paginator(specialFieldInfos, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        specialFieldInfos_page = self.paginator.page(self.currentPage)

        # 获取所有学院信息
        collegeInfos = CollegeInfo.objects.all()
        # 构造模板需要的参数
        context = {
            'collegeInfos': collegeInfos,
            'specialFieldInfos_page': specialFieldInfos_page,
            'specialFieldNumber': specialFieldNumber,
            'specialFieldName': specialFieldName,
            'specialCollegeNumber_collegeNumber': specialCollegeNumber_collegeNumber,
            'specialBirthDate': specialBirthDate,
            'currentPage': self.currentPage,
            'totalPage': self.totalPage,
            'recordNumber': self.recordNumber,
            'startIndex': self.startIndex,
            'pageList': self.pageList,
        }
        # 渲染模板界面
        return render(request, 'SpecialFieldInfo/specialFieldInfo_frontquery_result.html', context)


class FrontShowView(View):  # 前台显示专业信息详情页
    def get(self, request, specialFieldNumber):
        # 查询需要显示的专业信息对象
        specialFieldInfo = SpecialFieldInfo.objects.get(specialFieldNumber=specialFieldNumber)
        context = {
            'specialFieldInfo': specialFieldInfo
        }
        # 渲染模板显示
        return render(request, 'SpecialFieldInfo/specialFieldInfo_frontshow.html', context)


class ListAllView(View): # 前台查询所有专业信息
    def get(self,request):
        specialFieldInfos = SpecialFieldInfo.objects.all()
        specialFieldInfoList = []
        for specialFieldInfo in specialFieldInfos:
            specialFieldInfoObj = {
                'specialFieldNumber': specialFieldInfo.specialFieldNumber,
                'specialFieldName': specialFieldInfo.specialFieldName,
            }
            specialFieldInfoList.append(specialFieldInfoObj)
        return JsonResponse(specialFieldInfoList, safe=False)


class UpdateView(BaseView):  # Ajax方式专业信息更新
    def get(self, request, specialFieldNumber):
        # GET方式请求查询专业信息对象并返回专业信息json格式
        specialFieldInfo = SpecialFieldInfo.objects.get(specialFieldNumber=specialFieldNumber)
        return JsonResponse(specialFieldInfo.getJsonObj())

    def post(self, request, specialFieldNumber):
        # POST方式提交专业信息修改信息更新到数据库
        specialFieldInfo = SpecialFieldInfo.objects.get(specialFieldNumber=specialFieldNumber)
        specialFieldInfo.specialFieldName = request.POST.get('specialFieldInfo.specialFieldName')
        specialFieldInfo.specialCollegeNumber = CollegeInfo.objects.get(collegeNumber=request.POST.get('specialFieldInfo.specialCollegeNumber.collegeNumber'))
        specialFieldInfo.specialBirthDate = request.POST.get('specialFieldInfo.specialBirthDate')
        specialFieldInfo.specialMan = request.POST.get('specialFieldInfo.specialMan')
        specialFieldInfo.specialTelephone = request.POST.get('specialFieldInfo.specialTelephone')
        specialFieldInfo.specialMemo = request.POST.get('specialFieldInfo.specialMemo')
        specialFieldInfo.save()
        return JsonResponse({'success': True, 'message': '保存成功'})

class AddView(BaseView):  # 后台专业信息添加
    def primaryKeyExist(self, specialFieldNumber):  # 判断主键是否存在
        try:
            SpecialFieldInfo.objects.get(specialFieldNumber=specialFieldNumber)
            return True
        except SpecialFieldInfo.DoesNotExist:
            return False

    def get(self,request):
        collegeInfos = CollegeInfo.objects.all()  # 获取所有学院信息
        context = {
            'collegeInfos': collegeInfos,
        }

        # 渲染显示模板界面
        return render(request, 'SpecialFieldInfo/specialFieldInfo_add.html', context)

    def post(self, request):
        # POST方式处理图书添加业务
        specialFieldNumber = request.POST.get('specialFieldInfo.specialFieldNumber') # 判断专业编号是否存在
        if self.primaryKeyExist(specialFieldNumber):
            return JsonResponse({'success': False, 'message': '专业编号已经存在'})

        specialFieldInfo = SpecialFieldInfo() # 新建一个专业信息对象然后获取参数
        specialFieldInfo.specialFieldNumber = specialFieldNumber
        specialFieldInfo.specialFieldName = request.POST.get('specialFieldInfo.specialFieldName')
        specialFieldInfo.specialCollegeNumber = CollegeInfo.objects.get(collegeNumber=request.POST.get('specialFieldInfo.specialCollegeNumber.collegeNumber'))
        specialFieldInfo.specialBirthDate = request.POST.get('specialFieldInfo.specialBirthDate')
        specialFieldInfo.specialMan = request.POST.get('specialFieldInfo.specialMan')
        specialFieldInfo.specialTelephone = request.POST.get('specialFieldInfo.specialTelephone')
        specialFieldInfo.specialMemo = request.POST.get('specialFieldInfo.specialMemo')
        specialFieldInfo.save() # 保存专业信息信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class BackModifyView(BaseView):  # 后台更新专业信息
    def get(self, request, specialFieldNumber):
        context = {'specialFieldNumber': specialFieldNumber}
        return render(request, 'SpecialFieldInfo/specialFieldInfo_modify.html', context)


class ListView(BaseView):  # 后台专业信息列表
    def get(self, request):
        # 使用模板
        return render(request, 'SpecialFieldInfo/specialFieldInfo_query_result.html')

    def post(self, request):
        # 获取当前要显示第几页和每页几条数据
        self.getPageAndSize(request)
        # 收集查询参数
        specialFieldNumber = self.getStrParam(request, 'specialFieldNumber')
        specialFieldName = self.getStrParam(request, 'specialFieldName')
        specialCollegeNumber_collegeNumber = self.getStrParam(request, 'specialCollegeNumber.collegeNumber')
        specialBirthDate = self.getStrParam(request, 'specialBirthDate')
        # 然后条件组合查询过滤
        specialFieldInfos = SpecialFieldInfo.objects.all()
        if specialFieldNumber != '':
            specialFieldInfos = specialFieldInfos.filter(specialFieldNumber__contains=specialFieldNumber)
        if specialFieldName != '':
            specialFieldInfos = specialFieldInfos.filter(specialFieldName__contains=specialFieldName)
        if specialCollegeNumber_collegeNumber != '':
            specialFieldInfos = specialFieldInfos.filter(specialCollegeNumber=specialCollegeNumber_collegeNumber)
        if specialBirthDate != '':
            specialFieldInfos = specialFieldInfos.filter(specialBirthDate__contains=specialBirthDate)
        # 利用Paginator对查询结果集分页
        self.paginator = Paginator(specialFieldInfos, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        specialFieldInfos_page = self.paginator.page(self.currentPage)
        # 查询的结果集转换为列表
        specialFieldInfoList = []
        for specialFieldInfo in specialFieldInfos_page:
            specialFieldInfo = specialFieldInfo.getJsonObj()
            specialFieldInfoList.append(specialFieldInfo)
        # 构造模板页面需要的参数
        specialFieldInfo_res = {
            'rows': specialFieldInfoList,
            'total': self.recordNumber,
        }
        # 渲染模板页面显示
        return JsonResponse(specialFieldInfo_res, json_dumps_params={'ensure_ascii':False})

class DeletesView(BaseView):  # 删除专业信息信息
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        specialFieldNumbers = self.getStrParam(request, 'specialFieldNumbers')
        specialFieldNumbers = specialFieldNumbers.split(',')
        count = 0
        try:
            for specialFieldNumber in specialFieldNumbers:
                SpecialFieldInfo.objects.get(specialFieldNumber=specialFieldNumber).delete()
                count = count + 1
            message = '%s条记录删除成功！' % count
            success = True
        except Exception as e:
            message = '数据库外键约束删除失败！'
            success = False
        return JsonResponse({'success': success, 'message': message})


class OutToExcelView(BaseView):  # 导出专业信息信息到excel并下载
    def get(self, request):
        # 收集查询参数
        specialFieldNumber = self.getStrParam(request, 'specialFieldNumber')
        specialFieldName = self.getStrParam(request, 'specialFieldName')
        specialCollegeNumber_collegeNumber = self.getStrParam(request, 'specialCollegeNumber.collegeNumber')
        specialBirthDate = self.getStrParam(request, 'specialBirthDate')
        # 然后条件组合查询过滤
        specialFieldInfos = SpecialFieldInfo.objects.all()
        if specialFieldNumber != '':
            specialFieldInfos = specialFieldInfos.filter(specialFieldNumber__contains=specialFieldNumber)
        if specialFieldName != '':
            specialFieldInfos = specialFieldInfos.filter(specialFieldName__contains=specialFieldName)
        if specialCollegeNumber_collegeNumber != '':
            specialFieldInfos = specialFieldInfos.filter(specialCollegeNumber=specialCollegeNumber_collegeNumber)
        if specialBirthDate != '':
            specialFieldInfos = specialFieldInfos.filter(specialBirthDate__contains=specialBirthDate)
        #将查询结果集转换成列表
        specialFieldInfoList = []
        for specialFieldInfo in specialFieldInfos:
            specialFieldInfo = specialFieldInfo.getJsonObj()
            specialFieldInfoList.append(specialFieldInfo)
        # 利用pandas实现数据的导出功能
        pf = pd.DataFrame(specialFieldInfoList)
        # 设置要导入到excel的列
        columns_map = {
            'specialFieldNumber': '专业编号',
            'specialFieldName': '专业名称',
            'specialCollegeNumber': '所在学院',
            'specialBirthDate': '成立日期',
            'specialMan': '联系人',
            'specialTelephone': '联系电话',
        }
        pf = pf[columns_map.keys()]
        pf.rename(columns=columns_map, inplace=True)
        # 将空的单元格替换为空字符
        pf.fillna('', inplace=True)
        #设定文件名和导出路径
        filename = 'specialFieldInfos.xlsx'
        # 这个路径可以在settings中设置也可以直接手动输入
        root_path = settings.MEDIA_ROOT + '/output/'
        file_path = os.path.join(root_path, filename)
        pf.to_excel(file_path, encoding='utf-8', index=False)
        # 将生成的excel文件输出到网页下载
        file = open(file_path, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="specialFieldInfos.xlsx"'
        return response

