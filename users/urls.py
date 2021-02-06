from . import views
from django.urls import path

app_name='users'
urlpatterns = [
    path('teachers', views.teacherslist, name='teachers_list'),
    path('students', views.studentlist, name='student_list'),
    path('teacher/<int:pk>', views.teacherdetail, name='teacher_detail'),
    path('', views.home, name='home'),
    path('<pk>/delete', views.delete_teacher, name= 'delete_teacher' ), 
    path('<pk>/delete', views.delete_student, name= 'delete_student' ), 

]