from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

def sample(request):
    return HttpResponse("Hello World")

def sampleInfo(request):
    return HttpResponse("Welcome to Django Class")

def sample1(request):
    # data={"name":"Divya","age":21,"city":"Hyderabad"}
    data={"result":[10,20,30,40,50]}
    return JsonResponse(data,safe=False)

def dynamicResponse(request):
    name=request.GET.get("name",'')
    city=request.GET.get("city","hyderabad")
    return HttpResponse(f"Hello {name} from {city}")

def addition(request):
    num1=request.GET.get("num1",'')
    num2=request.GET.get("num2",'')
    return HttpResponse({num1+num2})

def subtraction(request):
    num1=request.GET.get("num1",'')
    num2=request.GET.get("num2",'')
    num1=int(num1)
    num2=int(num2)
    return HttpResponse({num1-num2})

def multiplication(request):
    num1=request.GET.get("num1",'')
    num2=request.GET.get("num2",'')
    num1=int(num1)
    num2=int(num2)
    return HttpResponse({num1*num2})

def division(request):
    num1=request.GET.get("num1",'')
    num2=request.GET.get("num2",'')
    num1=int(num1)
    num2=int(num2)
    return HttpResponse({num1%num2})