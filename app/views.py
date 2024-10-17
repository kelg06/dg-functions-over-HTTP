from django.shortcuts import render
from django.http import HttpResponse



def hello_view(request,name):
    return HttpResponse('Hey, ' + name+"!")

def age(request,end,birthyear):
    return HttpResponse(int(end) - int(birthyear))

def order(request,burgers,fries,drinks):
    totalB = float(burgers) * 4.50
    totalF = float(fries) * 1.50
    totalD = float(drinks) * 1
    total = totalD + totalF + totalB  
    return HttpResponse(total)