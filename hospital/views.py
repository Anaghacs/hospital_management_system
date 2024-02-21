from django.shortcuts import render

# Create your views here.

def index(request):
      return render(request,'index.html')

def home(request):
      return render(request,'home.html')

def navigation(request):
      return render(request, "navigation.html")

def contact(request):
      return render(request, "contact.html")
