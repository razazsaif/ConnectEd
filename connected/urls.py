from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.landing, name="landing"),
    path('home/', views.home, name="home"),
    path('learnerjoin/', views.learnerjoin, name="learnerjoin"),
    path('educatorjoin/', views.educatorjoin, name="educatorjoin"),
    path('login_view/', views.login_view, name="login_view"),
    path('user_logout/', views.user_logout, name="user_logout"),
    path('EnrollStd/', views.EnrollStd, name="EnrollStd"),
    path('add_course/', views.add_course, name="add_course"),
    path('courses_list/', views.courses_list, name="courses_list"),
    path('search/', views.search, name="search"),
 ]

