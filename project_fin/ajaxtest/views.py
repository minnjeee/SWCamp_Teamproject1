
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def ajax1(request): 
    return render(request, "ajax/ajaxtest1.html")

def result(request): 
    return JsonResponse({"result": "AjaxTest"})

