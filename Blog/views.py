from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import EntradaDeBlog
from django.urls import reverse_lazy, reverse
from django.contrib.auth import views as auth_views


class CreateEntradaDeBlog(LoginRequiredMixin, CreateView):
    model = EntradaDeBlog
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'imagen']
    template_name = 'Blog/create_entrada_blog.html'
    success_url = reverse_lazy('lista_de_entradas')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class EditEntradaDeBlog(LoginRequiredMixin, UpdateView):
    model = EntradaDeBlog
    fields = ['titulo', 'subtitulo', 'cuerpo', 'autor', 'imagen']
    template_name = 'Blog/edit_entrada_blog.html'
    success_url = reverse_lazy('lista_de_entradas')

class DeleteEntradaDeBlog(LoginRequiredMixin, DeleteView):
    model = EntradaDeBlog
    template_name = 'Blog/delete_entrada_blog.html'
    success_url = reverse_lazy('lista_de_entradas')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return redirect(success_url)


class EntradaDeBlog(ListView):
    model = EntradaDeBlog
    template_name = 'Blog/lista_de_entradas.html'
    success_url = reverse_lazy('lista_de_entradas')


def inicio(request):
    return render(
        request=request,
        template_name='Blog/inicio.html',
    )

def AboutMe(request):
    return render(
        request=request,
        template_name='Blog/sobre_mi.html',
    )


