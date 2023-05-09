from django.views.generic import View
from apps.BaseView import BaseView
from django.shortcuts import render
from django.core.paginator import Paginator
from apps.CollegeInfo.models import CollegeInfo
from django.http import JsonResponse
from django.http import FileResponse
from apps.BaseView import ImageFormatException
from django.conf import settings
import pandas as pd
import os


class FrontAddView(BaseView):  # 前台学院信息添加
    def primaryKeyExist(self, collegeNumber):  # 判断主键是否存在
        try:
            CollegeInfo.objects.get(collegeNumber=collegeNumber)
            return True
        except CollegeInfo.DoesNotExist:
            return False

    def get(self,request):

        # 使用模板
        return render(request, 'CollegeInfo/collegeInfo_frontAdd.html')

    def post(self, request):
        collegeNumber = request.POST.get('collegeInfo.collegeNumber') # 判断学院编号是否存在
        if self.primaryKeyExist(collegeNumber):
            return JsonResponse({'success': False, 'message': '学院编号已经存在'})

        collegeInfo = CollegeInfo() # 新建一个学院信息对象然后获取参数
        collegeInfo.collegeNumber = collegeNumber
        collegeInfo.collegeName = request.POST.get('collegeInfo.collegeName')
        collegeInfo.collegeBirthDate = request.POST.get('collegeInfo.collegeBirthDate')
        collegeInfo.collegeMan = request.POST.get('collegeInfo.collegeMan')
        collegeInfo.collegeTelephone = request.POST.get('collegeInfo.collegeTelephone')
        collegeInfo.collegeMemo = request.POST.get('collegeInfo.collegeMemo')
        collegeInfo.save() # 保存学院信息信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class FrontModifyView(BaseView):  # 前台修改学院信息
    def get(self, request, collegeNumber):
        context = {'collegeNumber': collegeNumber}
        return render(request, 'CollegeInfo/collegeInfo_frontModify.html', context)


class FrontListView(BaseView):  # 前台学院信息查询列表
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        self.getCurrentPage(request)  # 获取当前要显示第几页
        # 下面获取查询参数
        # 然后条件组合查询过滤
        collegeInfos = CollegeInfo.objects.all()
        # 对查询结果利用Paginator进行分页
        self.paginator = Paginator(collegeInfos, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        collegeInfos_page = self.paginator.page(self.currentPage)

        # 构造模板需要的参数
        context = {
            'collegeInfos_page': collegeInfos_page,
            'currentPage': self.currentPage,
            'totalPage': self.totalPage,
            'recordNumber': self.recordNumber,
            'startIndex': self.startIndex,
            'pageList': self.pageList,
        }
        # 渲染模板界面
        return render(request, 'CollegeInfo/collegeInfo_frontquery_result.html', context)


class FrontShowView(View):  # 前台显示学院信息详情页
    def get(self, request, collegeNumber):
        # 查询需要显示的学院信息对象
        collegeInfo = CollegeInfo.objects.get(collegeNumber=collegeNumber)
        context = {
            'collegeInfo': collegeInfo
        }
        # 渲染模板显示
        return render(request, 'CollegeInfo/collegeInfo_frontshow.html', context)


class ListAllView(View): # 前台查询所有学院信息
    def get(self,request):
        collegeInfos = CollegeInfo.objects.all()
        collegeInfoList = []
        for collegeInfo in collegeInfos:
            collegeInfoObj = {
                'collegeNumber': collegeInfo.collegeNumber,
                'collegeName': collegeInfo.collegeName,
            }
            collegeInfoList.append(collegeInfoObj)
        return JsonResponse(collegeInfoList, safe=False)


class UpdateView(BaseView):  # Ajax方式学院信息更新
    def get(self, request, collegeNumber):
        # GET方式请求查询学院信息对象并返回学院信息json格式
        collegeInfo = CollegeInfo.objects.get(collegeNumber=collegeNumber)
        return JsonResponse(collegeInfo.getJsonObj())

    def post(self, request, collegeNumber):
        # POST方式提交学院信息修改信息更新到数据库
        collegeInfo = CollegeInfo.objects.get(collegeNumber=collegeNumber)
        collegeInfo.collegeName = request.POST.get('collegeInfo.collegeName')
        collegeInfo.collegeBirthDate = request.POST.get('collegeInfo.collegeBirthDate')
        collegeInfo.collegeMan = request.POST.get('collegeInfo.collegeMan')
        collegeInfo.collegeTelephone = request.POST.get('collegeInfo.collegeTelephone')
        collegeInfo.collegeMemo = request.POST.get('collegeInfo.collegeMemo')
        collegeInfo.save()
        return JsonResponse({'success': True, 'message': '保存成功'})

class AddView(BaseView):  # 后台学院信息添加
    def primaryKeyExist(self, collegeNumber):  # 判断主键是否存在
        try:
            CollegeInfo.objects.get(collegeNumber=collegeNumber)
            return True
        except CollegeInfo.DoesNotExist:
            return False

    def get(self,request):

        # 渲染显示模板界面
        return render(request, 'CollegeInfo/collegeInfo_add.html')

    def post(self, request):
        # POST方式处理图书添加业务
        collegeNumber = request.POST.get('collegeInfo.collegeNumber') # 判断学院编号是否存在
        if self.primaryKeyExist(collegeNumber):
            return JsonResponse({'success': False, 'message': '学院编号已经存在'})

        collegeInfo = CollegeInfo() # 新建一个学院信息对象然后获取参数
        collegeInfo.collegeNumber = collegeNumber
        collegeInfo.collegeName = request.POST.get('collegeInfo.collegeName')
        collegeInfo.collegeBirthDate = request.POST.get('collegeInfo.collegeBirthDate')
        collegeInfo.collegeMan = request.POST.get('collegeInfo.collegeMan')
        collegeInfo.collegeTelephone = request.POST.get('collegeInfo.collegeTelephone')
        collegeInfo.collegeMemo = request.POST.get('collegeInfo.collegeMemo')
        collegeInfo.save() # 保存学院信息信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class BackModifyView(BaseView):  # 后台更新学院信息
    def get(self, request, collegeNumber):
        context = {'collegeNumber': collegeNumber}
        return render(request, 'CollegeInfo/collegeInfo_modify.html', context)


class ListView(BaseView):  # 后台学院信息列表
    def get(self, request):
        # 使用模板
        return render(request, 'CollegeInfo/collegeInfo_query_result.html')

    def post(self, request):
        # 获取当前要显示第几页和每页几条数据
        self.getPageAndSize(request)
        # 收集查询参数
        # 然后条件组合查询过滤
        collegeInfos = CollegeInfo.objects.all()
        # 利用Paginator对查询结果集分页
        self.paginator = Paginator(collegeInfos, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        collegeInfos_page = self.paginator.page(self.currentPage)
        # 查询的结果集转换为列表
        collegeInfoList = []
        for collegeInfo in collegeInfos_page:
            collegeInfo = collegeInfo.getJsonObj()
            collegeInfoList.append(collegeInfo)
        # 构造模板页面需要的参数
        collegeInfo_res = {
            'rows': collegeInfoList,
            'total': self.recordNumber,
        }
        # 渲染模板页面显示
        return JsonResponse(collegeInfo_res, json_dumps_params={'ensure_ascii':False})

class DeletesView(BaseView):  # 删除学院信息信息
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        collegeNumbers = self.getStrParam(request, 'collegeNumbers')
        collegeNumbers = collegeNumbers.split(',')
        count = 0
        try:
            for collegeNumber in collegeNumbers:
                CollegeInfo.objects.get(collegeNumber=collegeNumber).delete()
                count = count + 1
            message = '%s条记录删除成功！' % count
            success = True
        except Exception as e:
            message = '数据库外键约束删除失败！'
            success = False
        return JsonResponse({'success': success, 'message': message})


class OutToExcelView(BaseView):  # 导出学院信息信息到excel并下载
    def get(self, request):
        # 收集查询参数
        # 然后条件组合查询过滤
        collegeInfos = CollegeInfo.objects.all()
        #将查询结果集转换成列表
        collegeInfoList = []
        for collegeInfo in collegeInfos:
            collegeInfo = collegeInfo.getJsonObj()
            collegeInfoList.append(collegeInfo)
        # 利用pandas实现数据的导出功能
        pf = pd.DataFrame(collegeInfoList)
        # 设置要导入到excel的列
        columns_map = {
            'collegeNumber': '学院编号',
            'collegeName': '学院名称',
            'collegeBirthDate': '成立日期',
            'collegeMan': '院长姓名',
            'collegeTelephone': '联系电话',
        }
        pf = pf[columns_map.keys()]
        pf.rename(columns=columns_map, inplace=True)
        # 将空的单元格替换为空字符
        pf.fillna('', inplace=True)
        #设定文件名和导出路径
        filename = 'collegeInfos.xlsx'
        # 这个路径可以在settings中设置也可以直接手动输入
        root_path = settings.MEDIA_ROOT + '/output/'
        file_path = os.path.join(root_path, filename)
        pf.to_excel(file_path, encoding='utf-8', index=False)
        # 将生成的excel文件输出到网页下载
        file = open(file_path, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="collegeInfos.xlsx"'
        return response

