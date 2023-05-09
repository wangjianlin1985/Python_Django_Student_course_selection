from django.contrib import admin
from apps.CourseInfo.models import CourseInfo

# Register your models here.

admin.site.register(CourseInfo,admin.ModelAdmin)