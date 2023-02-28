from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Profile
from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'Usuarios/signup.html'

class LoginView(TemplateView):
    template_name = 'Usuarios/login.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('inicio')
        return render(request, self.template_name, {'form': form})


class ProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['User','Nombre', 'Apellido','Edad'] 
    template_name = 'Usuarios/profile.html'
    success_url = reverse_lazy('inicio')