from django.contrib import admin
from django.urls import path, include
from base.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('signin/', SigninView.as_view(), name='signin'),
    path('events/', EventsView.as_view(), name='events'),
    path('event/<int:eid>/', EventView.as_view(), name='event'),
    path('logout/', logout_view, name='logout'),
    path('Projects/', ProjectsView.as_view(), name='projects'),
    path('project/<int:pid>/', ProjectView.as_view(), name='project'),
    path('participate/<int:pid>/', participate, name='participate'),
]
