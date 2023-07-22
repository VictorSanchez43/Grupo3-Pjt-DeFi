from django.urls import path, include
from core import views

urlpatterns = [
    path('index/', views.indexView, name='index')
]