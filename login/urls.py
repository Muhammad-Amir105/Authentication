from django.urls import path
from . import views

urlpatterns = [
    path('add_task/' , views.add_task , name='add_task'),
    path('', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('todo-list/', views.todo_list, name='todo_list'),
    path('user_logout/' , views.user_logout , name='user_logout' ),
    
]
