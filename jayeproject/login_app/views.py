from django.shortcuts import render

# Create your views here.

def login (request):
    return render(request, "index.html")

def dashboard(request):
    return render(request, "dashboard.html")