from django.db import models
from apps.SpecialFieldInfo.models import SpecialFieldInfo


class ClassInfo(models.Model):
    classNumber = models.CharField(max_length=20, default='', primary_key=True, verbose_name='班级编号')
    className = models.CharField(max_length=20, default='', verbose_name='班级名称')
    classSpecialFieldNumber = models.ForeignKey(SpecialFieldInfo,  db_column='classSpecialFieldNumber', on_delete=models.PROTECT, verbose_name='所属专业')
    classBirthDate = models.CharField(max_length=20, default='', verbose_name='成立日期')
    classTeacherCharge = models.CharField(max_length=12, default='', verbose_name='班主任')
    classTelephone = models.CharField(max_length=20, default='', verbose_name='联系电话')
    classMemo = models.CharField(max_length=100, default='', verbose_name='附加信息')

    class Meta:
        db_table = 't_ClassInfo'
        verbose_name = '班级信息信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        classInfo = {
            'classNumber': self.classNumber,
            'className': self.className,
            'classSpecialFieldNumber': self.classSpecialFieldNumber.specialFieldName,
            'classSpecialFieldNumberPri': self.classSpecialFieldNumber.specialFieldNumber,
            'classBirthDate': self.classBirthDate,
            'classTeacherCharge': self.classTeacherCharge,
            'classTelephone': self.classTelephone,
            'classMemo': self.classMemo,
        }
        return classInfo

