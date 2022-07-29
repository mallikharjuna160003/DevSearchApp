from django.shortcuts import render,redirect
from .models import Project,Tag
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required
def project(request):
    projectslist = Project.objects.all()
    context = {'projects':projectslist}
    return render(request,'project/projects.html',context)

def single_project(request,pk):
    projectObj = Project.objects.get(id=pk)
    tags = Tag.objects.all()
    context={'project':projectObj,'tags':tags}
    return render(request,'project/single-project.html',context)
    
@login_required(login_url="login")
def createProject(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,"project/project_form.html",context)

@login_required(login_url="login")
def updateProject(request,pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,"project/project_form.html",context)

@login_required(login_url="login")
def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object':project}
    return render(request,'project/delete_template.html',context)