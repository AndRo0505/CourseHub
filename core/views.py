from django.shortcuts import render, get_object_or_404, redirect

from .forms import CourseForm
from .models import Course
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.

def home_redirect(request):
    return redirect('course_list')

def course_list(request):
    q = (request.GET.get('q') or '').strip()
    qs = Course.objects.all()
    if q:
        qs = qs.filter(Q(code__icontains=q) | Q(title__icontains=q))
    qs = qs.order_by('code')

    paginator = Paginator(qs, 10)
    page = request.GET.get('page')
    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)

    return render(request, 'core/courses_list.html', {'courses': courses, 'q': q})  # CHANGED

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'core/course_detail.html', {'course': course})

def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('course_detail', pk=course.pk)
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = CourseForm()
    return render(request, 'core/course_form.html', {'form': form, 'mode': 'create'})

def course_update(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            course = form.save()
            messages.success(request, f"Course {course.code} - {course.title} was updated.")
            return redirect('course_detail', pk=course.pk)
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = CourseForm(instance=course)
    return render(request, 'core/course_form.html', {'form': form, 'mode': 'edit', 'course': course})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        messages.success(request, f"Course {course.code} - {course.title} was deleted successfully.")
        return redirect('course_list')
    return redirect('course_detail', pk=course.pk)