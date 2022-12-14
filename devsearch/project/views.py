from django.shortcuts import render,redirect
from .models import Project,Tag
from .forms import ProjectForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .utils import searchProjects, paginateProjects
from django.contrib.auth.decorators import login_required

def project(request):
    projectslist,search_query = searchProjects(request)
    result = 3
    projectslist, custom_range = paginateProjects(request, projectslist, result)
    context = {'projects':projectslist,'search_query':search_query,'custom_range':custom_range}
    return render(request,'project/projects.html',context)

def single_project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = Tag.objects.all()
    context={'project':projectObj,'tags':tags}
    return render(request,'project/single-project.html',context)
    
@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile  

    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('account')
    context = {'form':form}
    return render(request,"project/project_form.html",context)

@login_required(login_url="login")
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form':form}
    return render(request,"project/project_form.html",context)

@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    context = {'object':project}
    return render(request,'delete_template.html',context)