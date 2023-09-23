from django.urls import path, include
from . import views
from rest_framework import routers
#  A router - allows us to create GET and POST requests. A GET Request gets a thing, it shows it on the screen, and a POST request posts something 
# to the database.

# Setup our router
router = routers.DefaultRouter()
#  register our router 
#  How we can access this courses URL From the webpage, as this is the URL we want to show.
router.register('courses', views.CourseView)

urlpatterns = [
    path('', include(router.urls)),
]
