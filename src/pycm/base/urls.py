from django.contrib import admin
from django.urls import path, include
from base.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', HomeView.as_view()),
    path('signup/', SignupView.as_view()),
    path('signin/', SigninView.as_view()),
    path('events/', EventsView.as_view()),
    path('event/', EventsView.as_view()),
]
