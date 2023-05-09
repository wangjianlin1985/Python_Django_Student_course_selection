from django.db import models


class Teacher(models.Model):
    teacherNumber = models.CharField(max_length=20, default='', primary_key=True, verbose_name='教师编号')
    teacherName = models.CharField(max_length=12, default='', verbose_name='教师姓名')
    teacherSex = models.CharField(max_length=2, default='', verbose_name='性别')
    teacherBirthday = models.CharField(max_length=20, default='', verbose_name='出生日期')
    teacherArriveDate = models.CharField(max_length=20, default='', verbose_name='入职日期')
    teacherCardNumber = models.CharField(max_length=20, default='', verbose_name='身份证号')
    teacherPhone = models.CharField(max_length=20, default='', verbose_name='联系电话')
    teacherPhoto = models.ImageField(upload_to='img', max_length='100', verbose_name='教师照片')
    teacherAddress = models.CharField(max_length=100, default='', verbose_name='家庭地址')
    teacherMemo = models.CharField(max_length=100, default='', verbose_name='附加信息')

    class Meta:
        db_table = 't_Teacher'
        verbose_name = '教师信息信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        teacher = {
            'teacherNumber': self.teacherNumber,
            'teacherName': self.teacherName,
            'teacherSex': self.teacherSex,
            'teacherBirthday': self.teacherBirthday,
            'teacherArriveDate': self.teacherArriveDate,
            'teacherCardNumber': self.teacherCardNumber,
            'teacherPhone': self.teacherPhone,
            'teacherPhoto': self.teacherPhoto.url,
            'teacherAddress': self.teacherAddress,
            'teacherMemo': self.teacherMemo,
        }
        return teacher

