from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.


class UsuarioLoginView(LoginView):
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('login') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))
    