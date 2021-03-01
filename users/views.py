from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from .models import Teacher,Student
from .forms import TeacherForm, StudentForm

def home(request):
    return render(request, 'home.html')

def teacherslist(request):
    teachers=Teacher.objects.all()
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=TeacherForm()

    return render(request, 'teachers.html', {'teachers': teachers, 'form':form})




def studentlist(request):
    student = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            studentz=form.save(commit=False)
            studentz.class_in=studentz.teacher.class_held
            studentz.save()
            print('formsaved')

        else:
            print(form.errors)
    else:
        form=StudentForm()

    return render(request, 'students.html', {'student': student, 'form':form})

# def studentlist(request):
#     student = Student.objects.all()
#     teacher =get_object_or_404(Teacher, class_held=class_held)
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             studentz=form.save(commit=False)
#             studentz.teacher=studentz.class_in.class_held
#             studentz.save()
#             print('formsaved')

#         else:
#             print(form.errors)
#     else:
#         form=StudentForm()

#     return render(request, 'students.html', {'student': student, 'form':form})



def teacherdetail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    mystudents = teacher.students.all()
    return render(request, 'teachetdetails.html', {'mystudents': mystudents, 'teacher':teacher})


def delete_teacher(request, pk): 
 
    context ={} 
    obj = get_object_or_404(Teacher, pk = pk) 
  
  
    if request.method =="POST": 
        obj.delete() 
        return HttpResponseRedirect("/teachers") 
  
    return render(request, "delete_view.html", context) 

def delete_student(request, pk): 
 
    context ={} 
    obj = get_object_or_404(Student, pk = pk) 
  
  
    if request.method =="POST": 
        obj.delete() 
        return HttpResponseRedirect("/students") 
  
    return render(request, "delete_view.html", context) 

def man (request):
    pass
