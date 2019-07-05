from django import forms
from home import models

class StudentEditModelForm(forms.ModelForm):
    class Meta:
        model=models.Student
        fields='__all__' # student_name,department
        #field=('department',)
        widgets={
            'student_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Student Name'}),
            'department':forms.Select(attrs={'class':'form-control'})
        }


class StudentCreateForm(forms.Form):
    student_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','maxlength':'50','placeholder':'Studentname'}))
    dept = (
        ('cse','computer science'),
        ('ise','information science'),
        ('mech','royalmech'),
        ('cl','civil engineering'),
    )
    department=forms.CharField(label='',widget=forms.Select(attrs={'class':'form-control'},choices=dept))

class StudentSearchForm(forms.Form):
    q=forms.CharField(label='',
    widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','placeholder':'search'}),
    )
    