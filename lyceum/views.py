from django.shortcuts import render, get_object_or_404, redirect
from .models import Teacher, Student, Parent
from .forms import TeacherForm, StudentForm, ParentForm

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'lyceum/teachers/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'lyceum/teachers/teacher_detail.html', {'teacher': teacher})

def teacher_create(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('teacher_list')
    return render(request, 'lyceum/teachers/teacher_form.html', {'form': form})

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    form = TeacherForm(request.POST or None, instance=teacher)
    if form.is_valid():
        form.save()
        return redirect('teacher_detail', pk=pk)
    return render(request, 'lyceum/teachers/teacher_form.html', {'form': form})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'lyceum/teachers/teacher_confirm_delete.html', {'teacher': teacher})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'lyceum/students/student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'lyceum/students/student_detail.html', {'student': student})

def student_create(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request, 'lyceum/students/student_form.html', {'form': form})

def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_detail', pk=pk)
    return render(request, 'lyceum/students/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'lyceum/students/student_confirm_delete.html', {'student': student})


# PARENT CRUD
def parent_list(request):
    parents = Parent.objects.all()
    return render(request, 'lyceum/parents/parent_list.html', {'parents': parents})

def parent_detail(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    return render(request, 'lyceum/parents/parent_detail.html', {'parent': parent})

def parent_create(request):
    form = ParentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('parent_list')
    return render(request, 'lyceum/parents/parent_form.html', {'form': form})

def parent_update(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    form = ParentForm(request.POST or None, instance=parent)
    if form.is_valid():
        form.save()
        return redirect('parent_detail', pk=pk)
    return render(request, 'lyceum/parents/parent_form.html', {'form': form})

def parent_delete(request, pk):
    parent = get_object_or_404(Parent, pk=pk)
    if request.method == 'POST':
        parent.delete()
        return redirect('parent_list')
    return render(request, 'lyceum/parents/parent_confirm_delete.html', {'parent': parent})