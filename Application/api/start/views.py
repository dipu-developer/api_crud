from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import Studentserializer
import io
from django.views.decorators.csrf import csrf_exempt
def registration(request,pk):
    reg = Student.objects.get(id=pk) #fatching the data by id
    serializer = Studentserializer(reg) #convet into serializer form
    json_data= JSONRenderer().render(serializer.data)   # convert into json data
    return HttpResponse(json_data,content_type='application/json')   # returing the content in json formate

def registration_all(request):
    reg = Student.objects.all()     #fatchin all the data 
    serializer = Studentserializer(reg, many=True)
    json_data= JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')      #returing the all the data


# This is the read api method
@csrf_exempt
def fatch_api(request):

    # fatching the data with api
    if request.method == 'GET':
        json_data = request.body    #fatching the data input by the user
        stream =io.BytesIO(json_data)   #converting the data into stream 
        python_data = JSONParser().parse(stream) # converting the data into python formate
        id  = python_data.get('id',None) # fatching the id 
        if id is not None:
            reg = Student.objects.get(id=id)    #getting the information through the id
            serializer = Studentserializer(reg) #converting into serializer form
            json_data = JSONRenderer().render(serializer.data)    #convertiong into json formate
            return HttpResponse(json_data,content_type='application/json')  #returing the data into json formate

        # this run when the usre need the whole data
        # or it call without id
        reg = Student.objects.all()    
        serializer = Studentserializer(reg, many=True)
        json_data= JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    # inserting the data with api
    if request.method =='POST':
        json_data = request.body    #fatching the data input by the user
        stream =io.BytesIO(json_data)   #converting the data into stream 
        python_data = JSONParser().parse(stream)
        print(python_data)
        serializer = Studentserializer(data= python_data)   #that data convertingg the data into serializer form 
        if serializer.is_valid():
            serializer.save()
            mes={'mess':"data insert sucessfully"}
            json_data = JSONRenderer().render(mes)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    # Updating the data with api

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id')
        reg= Student.objects.get(id=id)

        serializer = Studentserializer(reg,data=python_data,partial=True) #partial is true when we update the data in perticular colom
        # serializer = Studentserializer(reg,data=python_data) # by deafault partial is false that we we change whole the data column
        #if we don not give the whole column the serializer errors run and give the error worning

        if serializer.is_valid():
            serializer.save()
            mes={'mess':"data update sucessfully"}
            json_data= JSONRenderer().render(mes)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    # for deleting the data
    if request.method =='DELETE':
        json_data= request.body
        steam = io.BytesIO(json_data)
        python_data = JSONParser().parse(steam)
        id= python_data.get('id')
        reg = Student.objects.get(id=id)
        reg.delete()
        mes={'mess':"data delete sucessfully"}
        # json_data= JSONRenderer().render(mess)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(mes,safe=False)     # we can also use insted of this
