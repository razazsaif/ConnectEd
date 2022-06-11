from django.contrib import admin
from .models import Courses, Enroll, user_profile, educator_profile


# Register your models here.
admin.site.register(user_profile)
admin.site.register(educator_profile)
admin.site.register(Courses)
admin.site.register(Enroll)

