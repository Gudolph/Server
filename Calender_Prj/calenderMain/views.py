from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return redirect("http://127.0.0.1:3000/")
