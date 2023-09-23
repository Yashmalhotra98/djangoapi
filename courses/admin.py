from django.contrib import admin
#  From our models.py file import the Classes that we need
from .models import Course

# Register your models here.
#  We register our model with our admin section here.
admin.site.register(Course)