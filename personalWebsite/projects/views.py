from django.shortcuts import render, get_object_or_404
from projects.models import Project

def project_index(request):
    template_name = 'projects/index.html'

    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, template_name, context)

def project_detail(request, pk):
    template_name = 'projects/detail.html'
    project = get_object_or_404(Project, pk=pk)
    context = {
        'project': project
    }
    return render(request, template_name, context)

