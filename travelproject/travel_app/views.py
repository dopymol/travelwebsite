# from django.http import HttpResponse
from django.shortcuts import render
from .models import place,team_members

# Create your views here.

# def demo(request):
#     return HttpResponse('Hello World')

# def demo(request):
#     return render(request,"home.html")

def demo(request):
    obj=place.objects.all()
    obj1 = team_members.objects.all()
    return render(request, "index.html",{'results':obj,'name':obj1})

# def about(request):
#     return render(request,"about.html")
