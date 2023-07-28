from django.urls import path
from finanzas import views

app_name = 'finanzas'

urlpatterns = [
    path('finanzas/', views.VerFinanzas.as_view(), name='finanzas')
]