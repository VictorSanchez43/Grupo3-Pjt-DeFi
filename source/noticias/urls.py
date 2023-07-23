from django.urls import path
from noticias import views

app_name = 'noticias'

urlpatterns = [
    path('noticias/', views.VerNoticias.as_view(), name='noticias'),
]
