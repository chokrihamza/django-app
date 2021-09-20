# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context={
        'name':'jhon',
        'last_name':'doe',
        'age':20
    }
    return render(request,'index.html',context)