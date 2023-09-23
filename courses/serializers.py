#  A serializer takes data from a database and serializes it into a supported web data fromat, in our case i.e. JSON, which most APIs use to send 
# data around the internet. So, serializer, doesn't just creates it translates our data to and from JSON,  
from rest_framework import serializers
#  Import our models
from .models import Course

# class CourseSerializer(serializers.ModelSerializer):
class CourseSerializer(serializers.HyperlinkedModelSerializer):
    # By Adding a HyperlinkedModelSerializer, we can add a hyperlink to each of the bject returned by our API
    class Meta:
        model = Course # What model to use.
        # fields required in our API i.e. Id, name, language, price.
        #  We didn't put this in our model, but it does it anyway because whenever we put something in our database, it always gives an ID number,
        #  An ID number is automatically given to it 
        # name, language, price are taken straight from the model
        # fields = ('id', 'name', 'language', 'price')
        fields = ('id', 'url', 'name', 'language', 'price')
        #  We need to store the hyper link url in the url key-variable to store the hyperlink url