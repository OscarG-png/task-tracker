from django.shortcuts import render
from projects.models import Project


# Create your views here.
def show_projects(request):
    projects_list = Project.objects.all()
    context = {
        "projects_list": projects_list,
    }
    return render(request, "projects/list.html", context)
