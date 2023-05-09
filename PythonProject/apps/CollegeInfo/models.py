from django.db import models


class CollegeInfo(models.Model):
    collegeNumber = models.CharField(max_length=20, default='', primary_key=True, verbose_name='学院编号')
    collegeName = models.CharField(max_length=20, default='', verbose_name='学院名称')
    collegeBirthDate = models.CharField(max_length=20, default='', verbose_name='成立日期')
    collegeMan = models.CharField(max_length=10, default='', verbose_name='院长姓名')
    collegeTelephone = models.CharField(max_length=20, default='', verbose_name='联系电话')
    collegeMemo = models.CharField(max_length=100, default='', verbose_name='附加信息')

    class Meta:
        db_table = 't_CollegeInfo'
        verbose_name = '学院信息信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        collegeInfo = {
            'collegeNumber': self.collegeNumber,
            'collegeName': self.collegeName,
            'collegeBirthDate': self.collegeBirthDate,
            'collegeMan': self.collegeMan,
            'collegeTelephone': self.collegeTelephone,
            'collegeMemo': self.collegeMemo,
        }
        return collegeInfo

