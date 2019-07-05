from django.shortcuts import render,redirect
from home.forms import StudentSearchForm,StudentEditModelForm,StudentCreateForm
from home.models import Student
from django.contrib import messages
# Create your views here.

def home_view(request):
       # del request.session['id']
        #if request.session['id']==1:
        if request.method=='POST':
                search=StudentSearchForm(request.POST)
                print(search)
                if search.is_valid():
                        value=search.cleaned_data.get('q')
                        print(value)
                        result=Student.objects.filter(student_name__contains=value)
                        return render(request,'home.html',{'result':result})

        else:
                form=StudentSearchForm()
                result=Student.objects.all()
                return render(request,'home.html',{'form':form,'result':result})

def deletestudent(request,id):
    result=Student.objects.get(id=id)
    result.delete()
    messages.success(request,'deleted successfuly')
    return redirect('/')

def editstudent(request,id):
        #request.session['id']==id
        student= Student.objects.get(id=id)
        if request.method=='POST':
                modelform=StudentEditModelForm(request.POST,instance=student)
                if modelform.is_valid():
                        modelform.save()
                        return redirect('/')
        else:
                modelform=StudentEditModelForm(instance=student)
                return render(request,'edit.html',{'form':modelform})
    #form=StudentSearchForm()
    #msg="hello form django"
    #return render(request,'home.html',{'form':form,'msg':msg})

def createstudent(request):
        if request.method=="POST":
                form=StudentCreateForm(request.POST)
                if form.is_valid():
                        student=Student.objects.create(student_name=form.cleaned_data.get('student_name'),department=form.cleaned_data.get('department'))
                        student.save()
                        messages.success(request,'Created Succesufully!!')
                        return redirect('/')
        else:
                form=StudentCreateForm()
                return render(request,'create.html',{'form':form})
     

def about(request):
    return render(request,'home.html')

