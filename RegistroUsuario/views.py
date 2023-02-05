from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

class UsuarioRegisterView(LoginView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        messages.success(self.request, f'Account created for {username}!')
        return redirect('login')

    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the error below.')
        return self.render_to_response(self.get_context_data(form=form))

