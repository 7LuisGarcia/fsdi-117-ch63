from django.shortcuts import render
from .models import Project
from django.shortcuts import render

def projects_view(request):
    projects_list = Project.objects.all().order_by('-year')
    context = {'projects': projects_list}
    return render(request, 'projects/projects.html', context)