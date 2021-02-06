from django.contrib import admin
from .models import Teacher, Student

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name','level', 'class_held')
    list_filter = ("class_held",)
    search_fields = ['first_name', 'last_name']
    # prepopulated_fields = {'slug': ('title',)}


class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name','class_in', 'teacher')
    list_filter = ("class_in",)
    search_fields = ['first_name', 'last_name']
    # prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Teacher, TeacherAdmin)

  
admin.site.register(Student, StudentAdmin)