from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('add/', views.add_student, name='add_student'),
     path('edit/<int:id>/', views.edit_student, name='edit_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
     path('login/', auth_views.LoginView.as_view(template_name='students/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
