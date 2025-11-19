from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.db import connection
import json
from django.views.decorators.csrf import csrf_exempt
from basic.models import Student,Users
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


#to test database connection
def health(request):
    try:
        with connection.cursor() as c:
            c.execute("SELECT 1")
        return JsonResponse({"status":"ok","db":"connected"})
    except Exception as e:
        return JsonResponse({"status":"error","db":str(e)})   

@csrf_exempt
def addstudent(request):
    if request.method =='POST':
        print(request.method)
        data=json.loads(request.body)
        student=Student.objects.create(
            name=data.get("name"),
            age=data.get("age"),
            email=data.get("email")
            )
        return JsonResponse({"status":"success","id":student.id},status=200)
    
    elif request.method == "GET":
        result=list(Student.objects.values())
        print(result)
        return JsonResponse({"status":"ok","data":result},status=200)
    
    elif request.method == "PUT":
        data=json.loads(request.body)
        ref_id=data.get("id")       #getting id
        new_email=data.get("email")     #getting email
        existing_student=Student.objects.get(id=ref_id)  #fetched the object as per the id
        # print(existing_student)
        existing_student.email=new_email        # updating with new email 
        existing_student.save()
        updated_data=Student.objects.filter(id=ref_id).values().first()
        
        return JsonResponse({"status":"data updated successfully","updated_data":updated_data},status=200)
    
    elif request.method == "DELETE":
        data=json.loads(request.body)
        ref_id=data.get("id") 
        get_deleting_data=Student.objects.filter(id=ref_id).values().first()
        to_be_delete=Student.objects.get(id=ref_id)
        to_be_delete.delete()
        return JsonResponse({"status":"success","message":"student record deleted successfully","deleted data":get_deleting_data},status=200)
    
    #get all records
    elif request.method == "GET":
        result=list(Student.objects.values())
        print(result)
        return JsonResponse({"status":"ok","data":result},status=200)
    #get a specific record by id 
    elif request.method == "GET":
        data=json.loads(request.body)
        ref_id=data.get("id")
        result=Student.objects.filter(id=ref_id).values().first()
        return JsonResponse({"status":"ok","dta":result},status=200)
    #filter by age>=20
    elif request.method == "GET":
        data=json.loads(request.body)
        ref_age=data.get("age")
        result=list(Student.objects.filter(age_gte=ref_age).values())
        return JsonResponse({"status":"ok","data":result},status=200)
    # filter by age<=25
    elif request.method == "GET":
        data=json.loads(request.body)
        ref_age=data.get("age")
        result=list(Student.objects.filter(age_lte=ref_age).values())
        return JsonResponse({"status":"ok","data":result},status=200)
    # order by name
    elif request.method =="GET":
        result=list(Student.objects.order_by("name").values())
        return JsonResponse({"status":"ok","data":result},status=200)
    # get unique ages
    elif request.method == "GET":
        result=list(Student.objects.values("age").distinct())
        return JsonResponse({"status":"ok","data":result},status=200)
    # count total students
    elif request.method == "GET":
        result=Student.objects.count()
        return JsonResponse({"status":"ok","data":result},status=200)
     
    return JsonResponse({"error":"use post method"},status=400)

def job1(request):
    return JsonResponse({"message":"U have successfully applied for job1"},status=200)
def job2(request):
    return JsonResponse({"message":"U have successfully applied for job2"},status=200)


@csrf_exempt
def signUp(request):
    if request.method=="POST":
        data=json.loads(request.body)
        print(data)
        user=Users.objects.create(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password')
            )
        return JsonResponse({"status":"success"},status=200)