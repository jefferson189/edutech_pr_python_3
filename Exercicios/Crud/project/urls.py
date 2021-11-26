"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from crud.views import home, form_prof, form_aluno, create, view_aluno, view_prof, edit_aluno, edit_prof, update_aluno, update_prof, delete_prof, delete_aluno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form_prof/', form_prof, name='form_prof'),
    path('form_aluno/', form_aluno, name='form_aluno'),
    path('create/', create, name='create'),
    path('view_aluno/<int:pk>/', view_aluno, name='view_aluno'),
    path('view_prof/<int:pk>/', view_prof, name='view_prof'),
    path('edit_aluno/<int:pk>/', edit_aluno, name='edit_aluno'),
    path('edit_prof/<int:pk>/', edit_prof, name='edit_prof'),
    path('update_prof/<int:pk>/', update_prof, name='update_prof'),
    path('update_aluno/<int:pk>/', update_aluno, name='update_aluno'),
    path('delete_aluno/<int:pk>/', delete_aluno, name='delete_aluno'),
    path('delete_prof/<int:pk>/', delete_prof, name='delete_prof'),
]
