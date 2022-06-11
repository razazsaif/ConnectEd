from cgitb import lookup
from django.shortcuts import render
from django.http import  HttpResponseRedirect
from connected import models
from connected import forms
from .forms import UserForm, UserProfileInfoForm, EducatorForm ,CourseForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from connected.models import Courses
from django.db.models import Q



def landing(request):
    return render(request,'connected/landing.html')


@login_required(login_url='login_view')
def home(request):
    return render(request,'connected/home.html')


def learnerjoin(request):

    joined = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        learner_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and learner_form.is_valid():
            user = user_form.save()
            user.save()

            learner_profile = learner_form.save(commit=False)
            learner_profile.user = user
            print(learner_profile.user)
            learner_profile.save()

            joined = True
            return HttpResponseRedirect(reverse('login_view'))

        else:
            print(user_form.errors, learner_form.errors)

    else:
        user_form = UserForm()
        learner_form = UserProfileInfoForm()

    return render(request, 'connected/learnerjoin.html', {"learnerjoin":learnerjoin,'user_form':user_form,'learner_form':learner_form})



def educatorjoin(request):

    joined = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        educator_form = EducatorForm(request.POST, request.FILES)

        if user_form.is_valid() and educator_form.is_valid():
            user = user_form.save()
            user.save()

            educator_profile = educator_form.save(commit=False)
            educator_profile.user = user
            print(educator_profile.user)
            educator_profile.save()

            joined = True
            return HttpResponseRedirect(reverse('login_view'))

        else:
            print(user_form.errors, educator_form.errors)

    else:
        user_form = UserForm()
        educator_form = EducatorForm()

    return render(request, 'connected/educatorjoin.html', {"educatorjoin":educatorjoin,'user_form':user_form,'educator_form':educator_form})



def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, "connected/login.html", {
                "message": "Invalid credentials."
                })

    else:
        return render(request, 'connected/login.html')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('landing'))



# customize only for staff from educators profile table
@login_required
def add_course(request):
    submitted = False
    if request.method=="POST":
        course_form= CourseForm(request.POST)
        if course_form.is_valid():
            course_form.save()
            return HttpResponseRedirect('/add_course?submitted=True')
    else:
        course_form= CourseForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'connected/courses.html', {'course_form':course_form, 'submitted':submitted} )


#to explore courses in home page
@login_required
def courses_list(request):
    course_list = Courses.objects.all()
    
    return render(request, 'connected/courses_list.html', {
        'course_list': course_list
    })


#no login required condition because we can do search from landing page without login
# but if you loged in and search from course list or home you have the link to enroll or do back to the list 
def search(request):
    if request.method=='GET':
        searched = request.GET.get('searched')
        if searched:
            lookup = (Q(course_name__icontains=searched) | Q(course_type__icontains=searched))
            courses = Courses.objects.filter(lookup)
            return render(request, 'connected/search.html', {
            'courses': courses
              })
        else:

            return render(request,'connected/search.html',{
                "message": "No information to show"
        })
    else:
        return render(request,'connected/search.html',{})




#######################################################

# enrollment function done by MALAZ

def EnrollStd(request):

  form_data=forms.UserPyment(request.POST or None)
  msg=''
  if form_data.is_valid():
       enroll=models.Enroll()
       enroll.TID = form_data.cleaned_data['Transaction_ID']
       enroll.conf_TID = form_data.cleaned_data['Confirm_Transaction_ID']
       enroll.phone_num = form_data.cleaned_data['Phone_Number']
       enroll.conf_ph = form_data.cleaned_data['Confirm_Phone_Number']   
       enroll.save()
       msg='data is saved'
       
  context={
        'formpyment':form_data,
        'msg':msg
    }
  return render(request,'connected/pyment.html',context)


    




