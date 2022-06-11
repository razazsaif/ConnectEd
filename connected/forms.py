from dataclasses import field
import email
from django import forms
from django.contrib.auth.models import User
from connected.models import * 
from django.forms import ModelForm
from .models import educator_profile, user_profile, User
from django.contrib.auth.forms import UserCreationForm


#the email in user system is not unique so i add a function
class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username', 'first_name','last_name', 'email', 'password1','password2')
        labels = {
            'password1':'Password',
            'password2':'confirm Password',
        }
        def clean_email(self):
            email = self.cleaned_data.get('email')
            username = self.cleaned_data.get('username')
            if email and User.objects.filter(email=email).exclude(username=username).exists():
                raise forms.ValidationError('Email addresses must be unique.')
            return email


class UserProfileInfoForm(forms.ModelForm):

    bio = forms.CharField(required=False)

    learner = 'learner'
    parent = 'parent'
    user_types = [
        (learner,'learner'),
        (parent,'parent'),
        ]
    user_type = forms.ChoiceField(required=True, choices=user_types)

    phone_num = forms.IntegerField(required=True)


    Khartoum = 'Khartoum'
    Bahri = 'Bahri'
    Omdurman = 'parent'
    location_types = [
        (Khartoum, 'Khartoum'),
        (Bahri, 'Bahri'),
        (Omdurman, 'Omdurman'),
    ]
    location_type = forms.ChoiceField(required=True, choices=location_types)

    male = 'male'
    female = 'female'
    none ='prefer_not_to_answer'
    gender_types = [
        (male,'male'),
        (female,'female'),
        (none,'prefer_not_to_answer'),
        ]
    gender_type = forms.ChoiceField(required=True, choices=gender_types)

    class Meta():
        model = user_profile
        fields = ('bio' ,'profile_pic' ,'user_type','phone_num','location_type','gender_type')


class EducatorForm(forms.ModelForm):
    phone_num = forms.IntegerField(required=True)
    
    Khartoum = 'Khartoum'
    Bahri = 'Bahri'
    Omdurman = 'parent'

    location_types = [
        (Khartoum, 'Khartoum'),
        (Bahri, 'Bahri'),
        (Omdurman, 'Omdurman'),
    ]
    location_type = forms.ChoiceField(required=True, choices=location_types)

    male = 'male'
    female = 'female'
    none ='prefer_not_to_answer'
    gender_types = [
        (male,'male'),
        (female,'female'),
        (none,'prefer_not_to_answer'),
        ]
    gender_type = forms.ChoiceField(required=True, choices=gender_types)

  
    School = 'School_level'
    undergraduate = 'Undergraduate_level'
    postgraduate = 'Postgraduate_level'
    Freelances = 'Freelances_level'
    teaching_levels = [
        (School, 'School_level'),
        (undergraduate, 'Undergraduate_level'),
        (postgraduate, 'Postgraduate_level'),
        (Freelances, 'Freelances_level'),
    ]
    teaching_level = forms.ChoiceField(required=True, choices=teaching_levels)


    Certificate = 'Certificate'
    Freelance = 'Freelance'
    none = 'prefer_not_to_answer'
    educational_degree_types = [
        (Certificate, 'Certificate'),
        (Freelance, 'Freelance'),
        (none, 'prefer_not_to_answer'),
    ]
    educational_degree_type = forms.ChoiceField(required=True, choices=educational_degree_types)
    subject = forms.CharField(required=True)

    none = 'NO_Experince'
    less_than_five = '1upto5years'
    fromsix_uptoten = '6upto10years'
    More_than11years = 'More_than11years'
    experience_levels = [
        (none, 'NO_Experince'),
        (less_than_five, '1upto5years'),
        (fromsix_uptoten, '6upto10years'),
        (More_than11years, 'More_than11years'),
    ]
    experience_level = forms.ChoiceField(
        required=True, choices=experience_levels)

    individuals = 'individuals'
    groups = 'groups'
    teaching_prefernece_types = [
        (individuals,'individuals'),
        (groups,'groups'),
        ]
    teaching_prefernece_type = forms.ChoiceField(required=True, choices=teaching_prefernece_types)

    cv = forms.FileField(required=True)
    educational_certificate = forms.FileField(required=True)
    experince_certificate = forms.FileField(required=True)
    optional_certificate = forms.FileField(required=True)

    bio = forms.CharField(required=False)
   
    class Meta():
        model = educator_profile
        fields = ('bio' , 'profile_pic', 'phone_num','location_type','gender_type','teaching_level','educational_degree_type','subject','experience_level','teaching_prefernece_type','cv','educational_certificate','experince_certificate','optional_certificate')





class CourseForm(ModelForm):
    course_name = forms.CharField(required=True)
    educator_name = forms.CharField(required=True)
    course_type = forms.CharField(required=True)
    course_duration = forms.CharField(required=True)
    course_schedule = forms.CharField(required=True)
    lesson_number = forms.IntegerField(required=True)
    class Meta:
        model = Courses
        fields = ('course_name', 'course_type' , 'course_duration' , 'course_schedule' ,'lesson_number' )


#########################################################

# payment form done by MALAZ

class UserPyment(forms.Form):
    Transaction_ID = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    Confirm_Transaction_ID = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'} ))
    Phone_Number= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}  ))
    Confirm_Phone_Number= forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}  ))
   
