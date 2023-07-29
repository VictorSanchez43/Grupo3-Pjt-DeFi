from django.shortcuts import render

# Create your views here.

def acercaDeView(request):
    return render(request, 'acerca_de/acerca_de.html', {})