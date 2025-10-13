from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
# Create your views here.

def home_redirect(request):
    return redirect('course_list')

def course_list(request):
    courses = Course.objects.order_by('code')
    return render(request, 'core/courses_list.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'core/course_detail.html', {'course': course})
