""" required imports for module functionality """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
