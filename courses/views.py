#  views are sort of the brains behind the scenes that tells Django what to do with the Web Pages.
#  Normally, We've to create a view or create a function for each webpage  we want to build.
# But We're using the Django Rest Framework and it builds it all for us, we just need to designate that and to a couple of things.

from django.shortcuts import render
from rest_framework import viewsets #  viewsets- are sets of pages the rest_framework will create for us.
from .models import Course
from .serializers import CourseSerializer # Importing CourseSerializer class in this file.


# Create your views here.
class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all() # We call name of the Model.objects inside the Model.all the objects using all() method
    # queryset is the model, it's our database, and what we need to do is pull all the data out of our database
    serializer_class = CourseSerializer