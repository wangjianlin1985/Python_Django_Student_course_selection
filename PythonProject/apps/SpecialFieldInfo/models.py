from django.db import models
from apps.CollegeInfo.models import CollegeInfo


class SpecialFieldInfo(models.Model):
    specialFieldNumber = models.CharField(max_length=20, default='', primary_key=True, verbose_name='专业编号')
    specialFieldName = models.CharField(max_length=20, default='', verbose_name='专业名称')
    specialCollegeNumber = models.ForeignKey(CollegeInfo,  db_column='specialCollegeNumber', on_delete=models.PROTECT, verbose_name='所在学院')
    specialBirthDate = models.CharField(max_length=20, default='', verbose_name='成立日期')
    specialMan = models.CharField(max_length=10, default='', verbose_name='联系人')
    specialTelephone = models.CharField(max_length=20, default='', verbose_name='联系电话')
    specialMemo = models.CharField(max_length=100, default='', verbose_name='附加信息')

    class Meta:
        db_table = 't_SpecialFieldInfo'
        verbose_name = '专业信息信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        specialFieldInfo = {
            'specialFieldNumber': self.specialFieldNumber,
            'specialFieldName': self.specialFieldName,
            'specialCollegeNumber': self.specialCollegeNumber.collegeName,
            'specialCollegeNumberPri': self.specialCollegeNumber.collegeNumber,
            'specialBirthDate': self.specialBirthDate,
            'specialMan': self.specialMan,
            'specialTelephone': self.specialTelephone,
            'specialMemo': self.specialMemo,
        }
        return specialFieldInfo

