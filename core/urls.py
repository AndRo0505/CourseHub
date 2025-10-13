from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home'),  # keep root working
    path('courses/', views.course_list, name='course_list'),
    path('courses/<int:pk>/', views.course_detail, name='course_detail'),
]
