from django.urls import path
from . import views 

urlpatterns=[
    path('', views.index, name="list"),
    path('update_task/<str:primarykey>/', views.updateTask, name= "update_task"),
    path('delete_task/<str:primarykey>/', views.deleteTask, name= "delete_task") ,
    path('complete_task/<str:primarykey>/', views.completeTask, name="complete_task")

]