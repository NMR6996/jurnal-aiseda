from django.contrib import admin
from journal.models import *


class AdminVolume(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_home')


class AdminArticle(admin.ModelAdmin):
    pass


admin.site.register(Volume, AdminVolume)
admin.site.register(Article, AdminArticle)

