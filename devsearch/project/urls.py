from django.urls import path
from . import views

urlpatterns = [
    path('',views.project,name="projects"),
    path('create-project/',views.createProject,name="createproject"),
    path('single-project/<str:pk>/',views.single_project,name="project"),
    path('update-project/<str:pk>/',views.updateProject,name="updateproject"),
    path('delete-project/<str:pk>/',views.deleteProject,name="deleteproject"),

]