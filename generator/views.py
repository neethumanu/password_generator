from django.shortcuts import render
from django.contrib import messages
#custom functions
from .utils import random_gen
from .models import Contact
# Create your views here.
def home(request):
    return render(request, 'home.html')

def generate_pass(request):
    #print(request.POST)
    if request.method == "POST":
        length = request.POST.get("length")
        ucase = request.POST.get("ucase")
        num = request.POST.get("num")
        s_char = request.POST.get("schar")
    print(length,ucase,num,s_char)
    val = random_gen(length=length,num=num,s_char=s_char,ucase=ucase)
    print(val)

    return render(request,'result.html' ,context={'val1':val})

def contact(request):

    if request.method =="POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email_adrs = request.POST.get("email")
        adrs=request.POST.get("adrs")
        dat=request.POST.get("date")
        res=request.POST.get("res")
        calbk=request.POST.get("callback")
        print(name,phone,email_adrs,adrs,dat,res,calbk)
        messages.success(request, 'Successfully submitted.')
        cn=Contact(Name=name,Phone=phone,Email=email_adrs,Address=adrs,Date=dat,Reason=res,Call_back=calbk)
        cn.save()
    # print(name,phone,email_adrs,adrs,dat,res,calbk)
    return render(request,'contact.html')
    

def about(request):
    return render(request,'about.html')
