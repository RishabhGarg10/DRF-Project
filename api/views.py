from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def students(request):
    students = {
        "name" : "John Doe",
        "age" : 25,
        "class" : "Computer Science"

    }
    return JsonResponse(students)    
