from django.contrib import admin

# Register your models here.

from .models import *

class MemberAdmin(admin.ModelAdmin):
    list_display = ['id', 'real_name', 'tz']

admin.site.register(Member, MemberAdmin)

admin.site.register(ActivityPeriods)