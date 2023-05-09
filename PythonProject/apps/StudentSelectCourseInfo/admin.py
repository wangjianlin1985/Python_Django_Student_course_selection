from django.contrib import admin
from apps.StudentSelectCourseInfo.models import StudentSelectCourseInfo

# Register your models here.

admin.site.register(StudentSelectCourseInfo,admin.ModelAdmin)