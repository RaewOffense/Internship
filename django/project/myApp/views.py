from django.shortcuts import render
from django.http import HttpResponse

def form(request):
    return render(request,"index.html")