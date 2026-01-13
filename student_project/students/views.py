
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Student
from django.db.models import Q



def add_student(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        department = request.POST['department']

        Student.objects.create(
            name=name,
            email=email,
            phone=phone,
            department=department
        )
        
        messages.success(request, "Student added successfully")    


        return redirect('student_list')

    return render(request, 'students/add_student.html')

@login_required
def student_list(request):
    query = request.GET.get('q')

    students = Student.objects.all()

    if query:
        students = students.filter(
            Q(name__icontains=query) |
            Q(email__icontains=query) |
            Q(department__icontains=query)
        )

    paginator = Paginator(students, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'students/student_list.html',
        {
            'page_obj': page_obj,
            'query': query
        }
    )



def edit_student(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.department = request.POST['department']
        student.save()

        return redirect('student_list')

    return render(request, 'students/edit_student.html', {'student': student})

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')


    




