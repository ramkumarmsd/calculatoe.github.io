from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import calculator
from .form import forms
from django.contrib import messages 
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def home(request):
    
    result = " "  
    if request.method == 'POST':
        no1 = int(request.POST.get('number1'))
        no2 = int(request.POST.get('number2'))
        ans = request.POST.get('answer')
        obj = calculator(number1=no1,number2=no2,answer=ans)
        obj.save()
        

        opr = request.POST.get('operator')         

        if opr == '+':
            result = no1 + no2
            
        elif opr == '-':
            result = no1 - no2
              
        elif opr == 'x':
            result = no1 * no2
                                    
        elif opr == '/':
            result = no1 // no2         
               
    return render(request,'home.html',{'result':result})   
    
def login_page(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request,username=name,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('home')
        
        else:
            messages.error(request,"Invalide username or password")
            return redirect('login')
    return render(request,'login.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('home')


def register(request):
    form = forms()
    if request.method == 'POST':
        form = forms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration success... You can login now!!!")
            return redirect('login')
    return render(request,'register.html',{'form':form})

def testing(request):
  alldata = calculator.objects.all()
  if (alldata != " "):
      return render(request,'activity.html',{'datas':alldata})
  else:
      return render(request,'activity.html')
      