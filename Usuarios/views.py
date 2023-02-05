from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Profile
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'Usuarios/signup.html'

class LoginView(TemplateView):
    template_name = 'Usuarios/login.html'

class ProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['User','Nombre', 'Apellido','Edad'] # Add fields for user profile here
    template_name = 'Usuarios/profile.html'
    success_url = reverse_lazy('inicio')