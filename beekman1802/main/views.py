from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from main.models import *

# Create your views here.

def NetSuiteconnector(request):
    listreg=Class_NetSuite("")
    data= listreg.res
    ctx={"nametittle":"Connection NetSuite","regs":data}

    return HttpResponse(data)
    #return render(request, 'NetSuiteconnector.html', ctx)


def index(request):
    ctx={"nametittle":"Hello, world. You're at the polls index."}
    return render(request, 'index.html', ctx)
