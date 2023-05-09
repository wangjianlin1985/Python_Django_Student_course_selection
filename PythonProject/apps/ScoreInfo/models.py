from django.db import models
from apps.CourseInfo.models import CourseInfo
from apps.Student.models import Student


class ScoreInfo(models.Model):
    scoreId = models.AutoField(primary_key=True, verbose_name='记录编号')
    studentNumber = models.ForeignKey(Student,  db_column='studentNumber', on_delete=models.PROTECT, verbose_name='学生')
    courseNumber = models.ForeignKey(CourseInfo,  db_column='courseNumber', on_delete=models.PROTECT, verbose_name='课程')
    scoreValue = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='成绩得分')
    studentEvaluate = models.CharField(max_length=30, default='', verbose_name='学生评价')

    class Meta:
        db_table = 't_ScoreInfo'
        verbose_name = '成绩信息信息'
        verbose_name_plural = verbose_name

    def getJsonObj(self):
        scoreInfo = {
            'scoreId': self.scoreId,
            'studentNumber': self.studentNumber.studentName,
            'studentNumberPri': self.studentNumber.studentNumber,
            'courseNumber': self.courseNumber.courseName,
            'courseNumberPri': self.courseNumber.courseNumber,
            'scoreValue': self.scoreValue,
            'studentEvaluate': self.studentEvaluate,
        }
        return scoreInfo

