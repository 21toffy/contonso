from django import forms
from .models import Teacher,Student

class TeacherForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'level', 'class_held']


        


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'teacher']


        

# class StudentForm(forms.ModelForm):

#     class Meta:
#         model = Student
#         fields = ['first_name', 'last_name', 'class_in']


        

