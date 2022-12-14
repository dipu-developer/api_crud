from rest_framework import serializers
from .models import Student
class Studentserializer(serializers.Serializer):
    name= serializers.CharField(max_length=100)
    email = serializers.EmailField()
    city= serializers.CharField(max_length=100)

    #This is for inserting or creatng the data from api method
    def create(self,validate_data):
        return Student.objects.create(**validate_data)
    # For updating the data through api
    def update(self, instance, validated_data):
        # print(instance.name)  you can cheak the befaor update
        instance.name = validated_data.get('name',instance.name)
        # print(instance.name) this can cheak after update
        instance.email = validated_data.get('email',instance.email)
        instance.city = validated_data.get('email',instance.city)
        instance.save()     # this is use to save the the data
        return instance