from django.contrib import admin
from apps.News.models import News

# Register your models here.

admin.site.register(News,admin.ModelAdmin)