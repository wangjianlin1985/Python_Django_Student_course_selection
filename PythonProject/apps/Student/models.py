from django.db import models
from apps.ClassInfo.models import ClassInfo


class Student(models.Model):
    studentNumber = models.CharField(max_length=30, default='', primary_key=True, verbose_name='学号')
    studentName = models.CharField(max_length=12, default='', verbose_name='姓名')
    studentPassword = models.CharField(max_length=30, default='', verbose_name='登录密码')
    studentSex = models.CharField(max_length=2, default='', verbose_name='性别')
    studentClassNumber = models.ForeignKey(ClassInfo,  db_column='studentClassNumber', on_delete=models.PROTECT, verbose_name='所在班级')
    studentBirthday = models.CharField(max_length=20, default='', verbose_name='出生日期')
    studentState = models.CharField(max_length=20, default='', verbose_name='政治面貌')
    studentPhoto = models.ImageField(upload_to='img', max_length='100', verbose_name='学生照片')
    studentTelephone = models.CharField(max_length=20, default='', verbose_name='联系电话')
    studentEmail = models.CharField(max_length=30, default='', verbose_name='学生邮箱')
    studentQQ = models.CharField(max_length=20, default='', verbose_name='联系qq')
    studentAddress = models.CharField(max_length=100, default='', verbose_name='家庭地址')
    studentMemo = models.CharField(max_length=100, default='', verbose_name='附加信息')

    class Meta:
        db_table = 't_Student'
        verbose_name = '学生信息信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        student = {
            'studentNumber': self.studentNumber,
            'studentName': self.studentName,
            'studentPassword': self.studentPassword,
            'studentSex': self.studentSex,
            'studentClassNumber': self.studentClassNumber.className,
            'studentClassNumberPri': self.studentClassNumber.classNumber,
            'studentBirthday': self.studentBirthday,
            'studentState': self.studentState,
            'studentPhoto': self.studentPhoto.url,
            'studentTelephone': self.studentTelephone,
            'studentEmail': self.studentEmail,
            'studentQQ': self.studentQQ,
            'studentAddress': self.studentAddress,
            'studentMemo': self.studentMemo,
        }
        return student

