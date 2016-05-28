#coding:utf-8
from django import forms
from itcastsubject.models import Page, Subject

class SubjectForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the subject name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # 内部类
    class Meta:
        # model建立表单和模型类的关联，fields里包含表单显示出来的字段
        model = Subject 
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # model建立表单和模型类的关联，排除exclude里包含的字段，其它字段显示
        model = Page
        exclude = ('subject',)
        #fields = ('title', 'url', 'views')