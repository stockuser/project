from django.contrib import admin
from itcastsubject.models import Subject, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'subject')

class SubjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

    
admin.site.register(Subject)
admin.site.register(Page, PageAdmin)
