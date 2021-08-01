from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def blender(request):
    return render(request, 'home/blender.html')