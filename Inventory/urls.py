
from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('scanner/', views.scanner, name='scanner'),
    path('robotics_lab/', views.robotics_lab, name='robotics_lab'),
    path('robotics_lab/alienware/', views.alienware, name='alienware'),
     path('robotics_lab/sparkfun/', views.sparkfun, name='sparkfun'),
    path('robotics_lab/teacherpack/', views.teacherpack, name='teacherpack'),
    path('robotics_lab/spheros/', views.spheros, name='spheros'),
]
