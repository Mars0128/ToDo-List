from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context={}
    context['name']='許文豪'
    return render(request,'index.html',context)

# 判斷是get 請求 還是post 請求


# def Hello(request):
#     return HttpResponse('Hello World')