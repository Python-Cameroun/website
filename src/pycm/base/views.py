from django.shortcuts import render, redirect
from django.views import View


class HomeView(View):
    """This is the view for Home page"""
    
    def get(self, request, *args, **kwargs):
        return render(self.request, "base/home.html")


class SignupView(View):
    """This is the view for signup"""
    
    def get(self, request, *args, **kwargs):
        print("serving signup")
        return render(self.request, "base/signup.html")
    
    
class SigninView(View):
    """This is the view for signup"""
    
    def get(self, request, *args, **kwargs):
        print("serving signup")
        return render(self.request, "base/signin.html")

    
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
