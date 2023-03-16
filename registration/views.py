from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView


# Create your views here.

class RegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('main')

class LoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('main')

def show_profile(request):
    user = request.user

@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    template_name = 'registration/profile.html'
    
    def get_object(self):
        return get_object_or_404(User, username=self.request.user.username)