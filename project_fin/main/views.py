from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main/main.html')

def login(request):
    return render(request, "main/login.html")

def signin(reqest):
    return render(reqest, "main/member_write.html")