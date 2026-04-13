from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from app1.models import students,deparments,faculty
from app1.forms import student_form,department_form,faculty_form

class homeView(View):
    def get(self, request):
        return render(request,'home.html')


class student_details(View):
    def get(self,request):
        data=students.objects.all()
        form=student_form()
        context={
            'data':data,
            'form':form
        }
        return render(request,'student_1.html',context)
    
    def post(self,request):
        if request.method=='POST':
            form=student_form(request.POST)
            if form.is_valid():
                form.save()
                # return redirect('home_page')
                return redirect('std_det')
            else:
                form=student_form()
            context={
                'form':form
            }
            return render(request,'student_1.html',context)


class department_details(View):
    def get(self,request):
        data=deparments.objects.all()
        form=department_form()
        context={
            'data':data,
            'form':form
        }
        return render(request,'department_1.html',context)
    
    def post(self,request):
        if request.method=='POST':
            form=department_form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('dept_det')
            else:
                form=department_form()
            context={
                'form':form
            }
            return render(request,'department_1.html',context)


class faculty_details(View):
    def get(self,request):
        data=faculty.objects.all()
        form=faculty_form()
        context={
            'data':data,
            'form':form
        }
        return render(request,'faculty_1.html',context)
    
    def post(self,request):
        if request.method=='POST':
            form=faculty_form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('fac_det')
            else:
                form=faculty_form()
            context={
                'form':form
            }
            return render(request,'faculty_1.html',context)