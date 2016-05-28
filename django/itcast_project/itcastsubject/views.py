from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from itcastsubject.models import Subject, Page


def index(request):
    subject_list = Subject.objects.order_by('-name')[:5]
    context_dict = {'categories': subject_list}
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
                page.subject = cat
                page.views = 0
                page.save()
                # probably better to use a redirect here.
                return index(request)
            else:
                print form.errors
    else:
        form = PageForm()

    context_dict = {'form': form, 'subject': cat}
    return render(request, 'itcastsubject/add_page.html', context_dict)

from itcastsubject.forms import UserForm, UserProfileForm


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'itcastsubject/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/itcastsubject/')
            else:
                return HttpResponse("Your itcastsubject account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'itcastsubject/login.html', {})


@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/itcastsubject/')


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")
