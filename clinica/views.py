from django.shortcuts import render

def home(request):
    return render(request, 'clinica/home.html') 


def presente(request):
    return render(request, 'clinica/presente.html')

def seupedido(request):
    return render(request, 'clinica/seupedido.html')