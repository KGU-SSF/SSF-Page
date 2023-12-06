from django.shortcuts import render, redirect
from .models import join
from django.contrib import messages
from django.http import JsonResponse

def index(request):
    return render(request, '/Users/seojun/vscode/ssf_django/mainpage/templates/main/index.html')

def register_submit(request):

    joins = join()

    name = request.GET['name']
    studentID = request.GET['email']
    phoneNumber = request.GET['phone']
    message = request.GET['message']
    
    joins.applications_name = name
    joins.apllications_studentID = studentID
    joins.applications_phoneNumber = phoneNumber
    joins.applications_text = message

    print("저장 성공!")
    joins.save()

    return redirect('/')