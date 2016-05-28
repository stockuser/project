from django.contrib import admin

# Register your models here.
from itcastsubject.models import Subject, Page
from itcastsubject.models import UserProfile


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'Subject', 'url')


class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Subject)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
