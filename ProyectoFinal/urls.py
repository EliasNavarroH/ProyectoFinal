"""ProyectoFinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from Blog.views import CreateEntradaDeBlog, EditEntradaDeBlog, DeleteEntradaDeBlog, inicio, AboutMe, EntradaDeBlog
from Blog.admin import admin
from Usuarios.views import UsuarioLoginView, LogoutView
from RegistroUsuario.views import UsuarioRegisterView

urlpatterns = [
    path('create/', CreateEntradaDeBlog.as_view(), name='create_entrada_blog'),
    path('edit/<int:pk>/', EditEntradaDeBlog.as_view(), name='edit_entrada_blog'),
    path('delete/<int:pk>/', DeleteEntradaDeBlog.as_view(), name='delete_entrada_blog'),
    path('Entry/', EntradaDeBlog.as_view(), name='lista_de_entradas'),
    path('', inicio, name='inicio'),
    path('about-me/', AboutMe, name='sobre_mi'),
    path('admin/', admin.site.urls),
    path('login', UsuarioLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('signup/', UsuarioRegisterView.as_view(), name='signup'),
]
