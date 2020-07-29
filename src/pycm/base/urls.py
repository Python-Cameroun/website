from django.contrib import admin
from django.urls import path, include
from base.views import *
from .models import Project

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('events/', EventsView.as_view(), name='events'),
    path('event/<int:eid>/', EventView.as_view(), name='event'),
    path('logout/', logout_view, name='logout'),
    path('profile/<str:email>',profile_view, name='profile'), 
    path('projects/', projects, name='projects'),
    path('members/', members, name='members'),
    path('project_members/<str:project_name>',project_members, name='project_members'),
]
