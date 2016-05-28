from django.shortcuts import render
from django.http import HttpResponse
from itcastsubject.models import Subject, Page

def index(request):
    subject_list = Subject.objects.order_by('-name')[:5]
    context_dict = {'categories':subject_list}
    return render(request, 'itcastsubject/index.html', context_dict)

def about(request):
    return HttpResponse("itcast says here is the about page!\
    	<br/><a href='/itcastsubject/'>Index</a>")


def showsubject(request, Subject_name_slug):
    context_dict = {}
    try:
        subjectitem = Subject.objects.get(slug=Subject_name_slug)
        context_dict['subject_name'] = subjectitem.name
        pages = Page.objects.filter(subject=subjectitem)
        context_dict['pages'] = pages
        context_dict['subject'] = subjectitem
    except Subject.DoesNotExist:
        print "Subject none"
    return render(request, 'itcastsubject/Subject.html', context_dict)

from itcastsubject.forms import SubjectForm

def add_subject(request): 
    print '***********************'
    print request.POST
    print '***********************'
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = SubjectForm()
    return render(request, 'itcastsubject/add_subject.html', {'form': form})


from itcastsubject.forms import PageForm

def add_page(request, subject_name_slug):
    try:
        cat = Subject.objects.get(slug=subject_name_slug)
    except Subject.DoesNotExist:
        cat = None

    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.subject= cat
                page.views = 0
                page.save()
                # probably better to use a redirect here.
                return index(request)
            else:
                print form.errors
    else:
        form = PageForm()

    context_dict = {'form':form, 'subject': cat}
    return render(request, 'itcastsubject/add_page.html', context_dict)