from django.shortcuts import render
from django.views.generic import ListView

from website.models import Student, ClassRoom


class StudentList(ListView):
    template_name = 'website/students.html'
    model = Student
    context_object_name = 'students'


class ClassRoomList(ListView):
    template_name = 'website/class_room.html'
    model = ClassRoom
    context_object_name = 'classes'
