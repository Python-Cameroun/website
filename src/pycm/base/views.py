from django.shortcuts import render, redirect, reverse
from django.views import View
from base.forms import SignUpForm
from base.models import User, Profile, Event, Feedback, EventMedia, EventContactInfo
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.utils.translation import gettext as _
from django.http import Http404
import traceback


class HomeView(View):
    """This is the view for Home page"""

    def get(self, request, *args, **kwargs):
        fea_event = Event.objects.filter(featured=True).last()
        ctx = {'event':fea_event}
        return render(self.request, "base/home.html", ctx)


class SignupView(View):
    """This is the view for signup"""

    def get(self, request, *args, **kwargs):
        form = SignUpForm()
        return render(request, 'base/signup.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username, password=password, email=email)
            profile = Profile.objects.create(user=user)

            return redirect(reverse('signin'))

        else:
            print('Error: ', form.errors)
        return render(request, 'base/signup.html', {'form': form})


class SigninView(View):
    """This is the view for signup"""

    def get(self, request, *args, **kwargs):
        return render(self.request, "base/signin.html")

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('home'))
        else:
            messages.add_message(request, messages.ERROR, _('Invalid email or password'))
        return render(request, 'base/signin.html')


class EventsView(View):
    """This is the view for signup"""

    def get(self, request, *args, **kwargs):
        return render(self.request, "base/events.html")


class EventView(View):
    """This is the view for signup"""

    def get(self, request, *args, **kwargs):
        eid = self.kwargs.get('eid')
        try:
            event = Event.objects.get(pk=eid)
        except:
            return Http404()
        
        info = EventContactInfo.objects.filter(event=event).last()
        
        should_login = False
        
        if self.request.user.is_authenticated:
            feeds = Feedback.objects.filter(event=event, user=self.request.user)
            if len(feeds) < 2:
                can_give = True
            else:
                can_give = False                
        else:
            can_give = False
            should_login = True
        
        ctx = {'event': event, 'info':info, 'can_give':can_give,
               'should_login':should_login}
        return render(self.request, "base/event.html", ctx)
    
    def post(self, request, *args, **kwargs):
        try:
            if not self.request.user.is_authenticated:
                return self.get(request, *args, **kwargs)
            
            event = self.get_event()
            if not event:
                return Http404()
            
            content = self.request.POST.get('content')
            feeds = Feedback.objects.filter(event=event, user=self.request.user)
            if len(feeds) < 2:
                Feedback.objects.create(user=self.request.user, event=event,
                                        content=content)                                
        except:
            traceback.print_exc()
            
        return self.get(request, *args, **kwargs)
            
    def get_event(self):
        eid = self.kwargs.get('eid')
        try:
            return Event.objects.get(pk=eid)
        except:
            return None


def logout_view(request):
    logout(request)

    return redirect(reverse('signin'))
