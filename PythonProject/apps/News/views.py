from django.views.generic import View
from apps.BaseView import BaseView
from django.shortcuts import render
from django.core.paginator import Paginator
from apps.News.models import News
from django.http import JsonResponse
from django.http import FileResponse
from apps.BaseView import ImageFormatException
from django.conf import settings
import pandas as pd
import os


class FrontAddView(BaseView):  # 前台新闻信息添加
    def get(self,request):

        # 使用模板
        return render(request, 'News/news_frontAdd.html')

    def post(self, request):
        news = News() # 新建一个新闻信息对象然后获取参数
        news.newsTitle = request.POST.get('news.newsTitle')
        news.newsContent = request.POST.get('news.newsContent')
        news.newsDate = request.POST.get('news.newsDate')
        try:
            news.newsPhoto = self.uploadImageFile(request,'news.newsPhoto')
        except ImageFormatException as ife:
            return JsonResponse({'success': False, 'message': ife.error})
        news.save() # 保存新闻信息信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class FrontModifyView(BaseView):  # 前台修改新闻信息
    def get(self, request, newsId):
        context = {'newsId': newsId}
        return render(request, 'News/news_frontModify.html', context)


class FrontListView(BaseView):  # 前台新闻信息查询列表
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        self.getCurrentPage(request)  # 获取当前要显示第几页
        # 下面获取查询参数
        newsTitle = self.getStrParam(request, 'newsTitle')
        newsDate = self.getStrParam(request, 'newsDate')
        # 然后条件组合查询过滤
        newss = News.objects.all()
        if newsTitle != '':
            newss = newss.filter(newsTitle__contains=newsTitle)
        if newsDate != '':
            newss = newss.filter(newsDate__contains=newsDate)
        # 对查询结果利用Paginator进行分页
        self.paginator = Paginator(newss, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        newss_page = self.paginator.page(self.currentPage)

        # 构造模板需要的参数
        context = {
            'newss_page': newss_page,
            'newsTitle': newsTitle,
            'newsDate': newsDate,
            'currentPage': self.currentPage,
            'totalPage': self.totalPage,
            'recordNumber': self.recordNumber,
            'startIndex': self.startIndex,
            'pageList': self.pageList,
        }
        # 渲染模板界面
        return render(request, 'News/news_frontquery_result.html', context)


class FrontShowView(View):  # 前台显示新闻信息详情页
    def get(self, request, newsId):
        # 查询需要显示的新闻信息对象
        news = News.objects.get(newsId=newsId)
        context = {
            'news': news
        }
        # 渲染模板显示
        return render(request, 'News/news_frontshow.html', context)


class ListAllView(View): # 前台查询所有新闻信息
    def get(self,request):
        newss = News.objects.all()
        newsList = []
        for news in newss:
            newsObj = {
                'newsId': news.newsId,
                'newsTitle': news.newsTitle,
            }
            newsList.append(newsObj)
        return JsonResponse(newsList, safe=False)


class UpdateView(BaseView):  # Ajax方式新闻信息更新
    def get(self, request, newsId):
        # GET方式请求查询新闻信息对象并返回新闻信息json格式
        news = News.objects.get(newsId=newsId)
        return JsonResponse(news.getJsonObj())

    def post(self, request, newsId):
        # POST方式提交新闻信息修改信息更新到数据库
        news = News.objects.get(newsId=newsId)
        news.newsTitle = request.POST.get('news.newsTitle')
        news.newsContent = request.POST.get('news.newsContent')
        news.newsDate = request.POST.get('news.newsDate')
        try:
            newsPhotoName = self.uploadImageFile(request, 'news.newsPhoto')
        except ImageFormatException as ife:
            return JsonResponse({'success': False, 'message': ife.error})
        if newsPhotoName != 'img/NoImage.jpg':
            news.newsPhoto = newsPhotoName
        news.save()
        return JsonResponse({'success': True, 'message': '保存成功'})

class AddView(BaseView):  # 后台新闻信息添加
    def get(self,request):

        # 渲染显示模板界面
        return render(request, 'News/news_add.html')

    def post(self, request):
        # POST方式处理图书添加业务
        news = News() # 新建一个新闻信息对象然后获取参数
        news.newsTitle = request.POST.get('news.newsTitle')
        news.newsContent = request.POST.get('news.newsContent')
        news.newsDate = request.POST.get('news.newsDate')
        try:
            news.newsPhoto = self.uploadImageFile(request,'news.newsPhoto')
        except ImageFormatException as ife:
            return JsonResponse({'success': False, 'message': ife.error})
        news.save() # 保存新闻信息信息到数据库
        return JsonResponse({'success': True, 'message': '保存成功'})


class BackModifyView(BaseView):  # 后台更新新闻信息
    def get(self, request, newsId):
        context = {'newsId': newsId}
        return render(request, 'News/news_modify.html', context)


class ListView(BaseView):  # 后台新闻信息列表
    def get(self, request):
        # 使用模板
        return render(request, 'News/news_query_result.html')

    def post(self, request):
        # 获取当前要显示第几页和每页几条数据
        self.getPageAndSize(request)
        # 收集查询参数
        newsTitle = self.getStrParam(request, 'newsTitle')
        newsDate = self.getStrParam(request, 'newsDate')
        # 然后条件组合查询过滤
        newss = News.objects.all()
        if newsTitle != '':
            newss = newss.filter(newsTitle__contains=newsTitle)
        if newsDate != '':
            newss = newss.filter(newsDate__contains=newsDate)
        # 利用Paginator对查询结果集分页
        self.paginator = Paginator(newss, self.pageSize)
        # 计算总的页码数，要显示的页码列表，总记录等
        self.calculatePages()
        # 获取第page页的Page实例对象
        newss_page = self.paginator.page(self.currentPage)
        # 查询的结果集转换为列表
        newsList = []
        for news in newss_page:
            news = news.getJsonObj()
            newsList.append(news)
        # 构造模板页面需要的参数
        news_res = {
            'rows': newsList,
            'total': self.recordNumber,
        }
        # 渲染模板页面显示
        return JsonResponse(news_res, json_dumps_params={'ensure_ascii':False})

class DeletesView(BaseView):  # 删除新闻信息信息
    def get(self, request):
        return self.handle(request)

    def post(self, request):
        return self.handle(request)

    def handle(self, request):
        newsIds = self.getStrParam(request, 'newsIds')
        newsIds = newsIds.split(',')
        count = 0
        try:
            for newsId in newsIds:
                News.objects.get(newsId=newsId).delete()
                count = count + 1
            message = '%s条记录删除成功！' % count
            success = True
        except Exception as e:
            message = '数据库外键约束删除失败！'
            success = False
        return JsonResponse({'success': success, 'message': message})


class OutToExcelView(BaseView):  # 导出新闻信息信息到excel并下载
    def get(self, request):
        # 收集查询参数
        newsTitle = self.getStrParam(request, 'newsTitle')
        newsDate = self.getStrParam(request, 'newsDate')
        # 然后条件组合查询过滤
        newss = News.objects.all()
        if newsTitle != '':
            newss = newss.filter(newsTitle__contains=newsTitle)
        if newsDate != '':
            newss = newss.filter(newsDate__contains=newsDate)
        #将查询结果集转换成列表
        newsList = []
        for news in newss:
            news = news.getJsonObj()
            newsList.append(news)
        # 利用pandas实现数据的导出功能
        pf = pd.DataFrame(newsList)
        # 设置要导入到excel的列
        columns_map = {
            'newsId': '记录编号',
            'newsTitle': '新闻标题',
            'newsContent': '新闻内容',
            'newsDate': '发布日期',
        }
        pf = pf[columns_map.keys()]
        pf.rename(columns=columns_map, inplace=True)
        # 将空的单元格替换为空字符
        pf.fillna('', inplace=True)
        #设定文件名和导出路径
        filename = 'newss.xlsx'
        # 这个路径可以在settings中设置也可以直接手动输入
        root_path = settings.MEDIA_ROOT + '/output/'
        file_path = os.path.join(root_path, filename)
        pf.to_excel(file_path, encoding='utf-8', index=False)
        # 将生成的excel文件输出到网页下载
        file = open(file_path, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="newss.xlsx"'
        return response

