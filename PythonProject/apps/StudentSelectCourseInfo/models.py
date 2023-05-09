from django.db import models
from apps.CourseInfo.models import CourseInfo
from apps.Student.models import Student


class StudentSelectCourseInfo(models.Model):
    selectId = models.AutoField(primary_key=True, verbose_name='记录编号')
    studentNumber = models.ForeignKey(Student,  db_column='studentNumber', on_delete=models.PROTECT, verbose_name='选课学生')
    courseNumber = models.ForeignKey(CourseInfo,  db_column='courseNumber', on_delete=models.PROTECT, verbose_name='选择课程')
    selectTime = models.CharField(max_length=20, default='', verbose_name='选课时间')

    class Meta:
        db_table = 't_StudentSelectCourseInfo'
        verbose_name = '选课信息信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        studentSelectCourseInfo = {
            'selectId': self.selectId,
            'studentNumber': self.studentNumber.studentName,
            'studentNumberPri': self.studentNumber.studentNumber,
            'courseNumber': self.courseNumber.courseName,
            'courseNumberPri': self.courseNumber.courseNumber,
            'selectTime': self.selectTime,
        }
        return studentSelectCourseInfo

