from django.shortcuts import render, redirect, reverse
from django.views import View
from base.forms import SignUpForm
from base.models import User, Profile
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.utils.translation import gettext as _


class HomeView(View):
    """This is the view for Home page"""

    def get(self, request, *args, **kwargs):
        return render(self.request, "base/home.html")


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
        print("serving signup")
        return render(self.request, "base/events.html")


class EventsView(View):
    """This is the view for signup"""

    def get(self, request, *args, **kwargs):
        print("serving signup")
        return render(self.request, "base/event.html")


def logout_view(request):
    logout(request)

    return redirect(reverse('signin'))
