from django.urls import path
from student.views import *
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
	path('',student_list, name='student_list'),
	path('<int:id>/details/',student_details,name='student_details'),
	path('add/', student_add, name='student_add'),
	path('<int:id>/edit/', student_edit, name='student_edit'),
	path('<int:id>/delete/', student_delete, name='student_delete'),
]