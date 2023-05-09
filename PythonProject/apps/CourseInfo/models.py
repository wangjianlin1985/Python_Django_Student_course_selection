from django.db import models
from apps.Teacher.models import Teacher


class CourseInfo(models.Model):
    courseNumber = models.CharField(max_length=20, default='', primary_key=True, verbose_name='课程编号')
    courseName = models.CharField(max_length=20, default='', verbose_name='课程名称')
    coursePhoto = models.ImageField(upload_to='img', max_length='100', verbose_name='课程图片')
    courseTeacher = models.ForeignKey(Teacher,  db_column='courseTeacher', on_delete=models.PROTECT, verbose_name='上课老师')
    courseTime = models.CharField(max_length=40, default='', verbose_name='上课时间')
    coursePlace = models.CharField(max_length=40, default='', verbose_name='上课地点')
    courseScore = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='课程学分')
    courseMemo = models.CharField(max_length=100, default='', verbose_name='附加信息')

    class Meta:
        db_table = 't_CourseInfo'
        verbose_name = '课程信息信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        courseInfo = {
            'courseNumber': self.courseNumber,
            'courseName': self.courseName,
            'coursePhoto': self.coursePhoto.url,
            'courseTeacher': self.courseTeacher.teacherName,
            'courseTeacherPri': self.courseTeacher.teacherNumber,
            'courseTime': self.courseTime,
            'coursePlace': self.coursePlace,
            'courseScore': self.courseScore,
            'courseMemo': self.courseMemo,
        }
        return courseInfo

