from django.db import models

# Create your models here.

class Student(models.Model):
    student_name=models.CharField('Student Name',max_length=30,null=True,unique=True)
    dept = (
        ('cse','computer science'),
        ('ise','information science'),
        ('mech','royalmech'),
        ('cl','civil engineering'),
    )

    department=models.CharField('Department',choices=dept,blank=True,null=True,max_length=30)
    
    timestamp=models.DateTimeField(auto_now_add=True)

class Library(models.Model):
    sut=models.ForeignKey('Student',on_delete=models.SET_NULL,null=True)