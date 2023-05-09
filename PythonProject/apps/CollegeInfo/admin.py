from django.contrib import admin
from apps.CollegeInfo.models import CollegeInfo

# Register your models here.

admin.site.register(CollegeInfo,admin.ModelAdmin)