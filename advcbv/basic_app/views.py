from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views.generic import DetailView
from . import models


class IndexView(TemplateView):
    template_name = 'index.html'


class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
 #   template_name = 'basic_app/school_list.html'


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'


class StudentListView(ListView):
    model = models.Student


class StudentDetailView(DetailView):
    model = models.Student
    template_name = 'basic_app/student_detail.html'

