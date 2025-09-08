from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm

# ---------------- HTML Views (MTV) ----------------
def student_list_html(request):
    """Render list of students in HTML template"""
    students = Student.objects.all().order_by('name')
    return render(request, 'students/student_list.html', {'students': students})

def add_student(request):
    """Add a new student via HTML form"""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students:list_html')
    else:
        form = StudentForm()
    return render(request, 'students/add_student.html', {'form': form})


# ---------------- DRF API Views ----------------
from rest_framework import viewsets
from .serializers import StudentSerializer
from rest_framework.permissions import AllowAny

class StudentViewSet(viewsets.ModelViewSet):
    """
    Provides list, retrieve, create, update, destroy for Student.
    """
    queryset = Student.objects.all().order_by('id')
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
