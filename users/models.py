from django.db import models
from django.contrib.auth.models import User
from model_utils import Choices


# CLASS = (
#     ("JSS1","Jss1"),
#     ("JSS2","Jss2"),
#     ("JSS3","Jss3"),
#     ("SSS1","Sss1"),
#     ("SSS2","Sss2"),
#     ("SSS3","Sss3"),
# )

class Teacher(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    level=models.IntegerField()
    CLASS = Choices('Jss1', 'Jss2', 'Jss3', 'Sss1', 'Sss2', 'Sss3')
    class_held = models.CharField(max_length=5 , choices=CLASS)

    def __str__(self):
        return self.first_name+" "+ self.last_name

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    class_in = models.CharField(max_length=5)
    teacher =models.ForeignKey(Teacher, blank=True, null=True, related_name='students', on_delete=models.SET_NULL)


    class Meta:
        ordering = ['-class_in']

    def __str__(self):
        return self.first_name+ " " +self.last_name


