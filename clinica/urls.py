# clinica/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('presente/', views.presente, name='presente'),
    path('seupedido/', views.seupedido, name='seupedido'),
]