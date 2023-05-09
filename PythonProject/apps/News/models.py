from django.db import models


class News(models.Model):
    newsId = models.AutoField(primary_key=True, verbose_name='记录编号')
    newsTitle = models.CharField(max_length=50, default='', verbose_name='新闻标题')
    newsContent = models.CharField(max_length=500, default='', verbose_name='新闻内容')
    newsDate = models.CharField(max_length=20, default='', verbose_name='发布日期')
    newsPhoto = models.ImageField(upload_to='img', max_length='100', verbose_name='新闻图片')

    class Meta:
        db_table = 't_News'
        verbose_name = '新闻信息信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        news = {
            'newsId': self.newsId,
            'newsTitle': self.newsTitle,
            'newsContent': self.newsContent,
            'newsDate': self.newsDate,
            'newsPhoto': self.newsPhoto.url,
        }
        return news

