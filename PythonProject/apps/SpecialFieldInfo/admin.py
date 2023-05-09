from django.contrib import admin
from apps.SpecialFieldInfo.models import SpecialFieldInfo

# Register your models here.

admin.site.register(SpecialFieldInfo,admin.ModelAdmin)