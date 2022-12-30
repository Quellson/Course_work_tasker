from django.urls import path
from . import views

urlpatterns = [
    path('', views.first,name ="home-page"),
    path('about-us-information',views.about, name ="about-page"),#watching url links you can add them here
    path('login-in',views.login ,name = "login"),
    path('tasker',views.tasks, name ="tasker-task-page"),
    path('create_task',views.create_task, name ="create_task")
]
