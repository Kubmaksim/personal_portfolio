from django.shortcuts import render
from .models import Project


def home(request):
    file = Project.objects.all()
    return render(request, "portfolio/home.html", {'block_file': file})
