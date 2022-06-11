from django.db import models
from django.contrib.auth.models import User
import os


 # save the profiles pics in particular folder with particular name

def path_and_rename(instance, filename):
    upload_to = 'Images/'
    ext = filename.split(".")[-1]
# get filename
    if instance.user.username:
        filename = 'User_Profile_Pictures/{}.{}'.format(
            instance.user.username, ext)
    return os.path.join(upload_to, filename)



# two user types models extend from the user model separately (for more future work changes)

# named the first one user not learner cause we have parent user type inside of it (for future featuers)

# work with choices to reduce the data cleaning later on


class user_profile(models.Model):

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
        
    bio = models.CharField(max_length=150, blank=True)
    profile_pic = models.ImageField(
        upload_to=path_and_rename, verbose_name="Profile Picture", blank=True)

    phone_num = models.IntegerField(blank=True, default=404)
   
    Khartoum = 'Khartoum'
    Bahri = 'Bahri'
    Omdurman = 'parent'
    location_types = [
        (Khartoum, 'Khartoum'),
        (Bahri, 'Bahri'),
        (Omdurman, 'Omdurman'),
    ]
    location_type = models.CharField(
        max_length=10, choices=location_types, default=Khartoum)

    male = 'male'
    female = 'female'
    none = 'prefer_not_to_answer'
    gender_types = [
        (male, 'male'),
        (female, 'female'),
        (none, 'prefer_not_to_answer'),
    ]
    gender_type = models.CharField(
        max_length=64, choices=gender_types, default=none)

    learner = 'learner'
    parent = 'parent'

    user_types = [
        (learner, 'learner'),
        (parent, 'parent'),
    ]
    user_type = models.CharField(
        max_length=10, choices=user_types, default=learner)

    def __str__(self):
        return self.user.username


# this model contain the initial educator who filled the form 
# so the admin can view there cv's and his other files to decide the staff 
# and there will be email notify for these functionality (still working on it)

class educator_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_num = models.IntegerField(blank=True, default=404)

    Khartoum = 'Khartoum'
    Bahri = 'Bahri'
    Omdurman = 'parent'
    location_types = [
        (Khartoum, 'Khartoum'),
        (Bahri, 'Bahri'),
        (Omdurman, 'Omdurman'),
    ]
    location_type = models.CharField(
        max_length=10, choices=location_types, default=Khartoum)

    male = 'male'
    female = 'female'
    none = 'prefer_not_to_answer'
    gender_types = [
        (male, 'male'),
        (female, 'female'),
        (none, 'prefer_not_to_answer'),
    ]
    gender_type = models.CharField(
        max_length=64, choices=gender_types, default=none)
  
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
    teaching_level = models.CharField(
        max_length=24, choices=teaching_levels, default=School)
   
    Certificate = 'Certificate'
    Freelance = 'Freelance'
    none = 'prefer_not_to_answer'
    educational_degree_types = [
        (Certificate, 'Certificate'),
        (Freelance, 'Freelance'),
        (none, 'prefer_not_to_answer'),
    ]
    educational_degree_type = models.CharField(
        max_length=64, choices=educational_degree_types, default=Certificate)
    subject = models.CharField(max_length=64, blank=True)

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
    experience_level = models.CharField(
        max_length=24, choices=experience_levels, default=none)

    individuals = 'individuals'
    groups = 'groups'
    teaching_prefernece_types = [
        (individuals, 'individuals'),
        (groups, 'groups'),
    ]
    teaching_prefernece_type = models.CharField(
        max_length=24, choices=teaching_prefernece_types, default=groups)

    cv = models.FileField(upload_to='cvs/pdfs/', default="")
    educational_certificate = models.FileField(upload_to='educational_certificates/pdfs/', default="")
    experince_certificate = models.FileField(upload_to='experince_certificate/pdfs/', default="")
    optional_certificate = models.FileField(upload_to='optional_certificate/pdfs/', default="")

    bio = models.CharField(max_length=150, blank=True)
    profile_pic = models.ImageField(upload_to=path_and_rename, verbose_name="Profile Picture", null=True, blank=True)

    def __str__(self):
        return f" {self.user.first_name} {self.user.last_name} "


class Courses(models.Model):
    course_name = models.CharField(max_length=64, default="")
    course_type = models.CharField(max_length=64, default="")
    course_duration = models.CharField(max_length=64, default="")
    course_schedule = models.CharField(max_length=64, default="")
    lesson_number = models.IntegerField(blank=True, default=0)
    educators = models.ManyToManyField(educator_profile, blank=True, related_name="teachers")
    learners = models.ManyToManyField(user_profile, blank=True, related_name="students")

    def __str__(self):
        return f" {self.id}: course name: {self.course_name} longs for {self.course_duration} "



class Erollment(models.Model):
    course_name = models.CharField(max_length=64, default="")
    course_type = models.CharField(max_length=64, default="")
    course_duration = models.CharField(max_length=64, default="")
    course_schedule = models.CharField(max_length=64, default="")
    lesson_number = models.IntegerField(blank=True, default=0)
    courses = models.ManyToManyField(Courses, blank=True, related_name="teachers")
    learners = models.ManyToManyField(user_profile, blank=True, related_name="students")

    def __str__(self):
        return f" {self.id}: course name: {self.course_name} longs for {self.course_duration} "




######################################################################################

# #Erollment model done by MALAZ
# class Enroll(models.Model):
#     TID = models.IntegerField()
#     conf_TID = models.IntegerField()
#     phone_num = models.CharField(max_length=15)
#     conf_ph = models.CharField(max_length=15)

# def __str__(self):
#     return self.TID