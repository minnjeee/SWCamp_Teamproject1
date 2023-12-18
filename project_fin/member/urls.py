from django.urls import path
from .import views

app_name="Member"

urlpatterns=[
    path("write", views.write), #회원가입폼으로 이동
    path("save", views.save), #회원가입
    path("idcheck", views.idcheck), #아이디중복체크
    path("logon", views.logon), #페이지 이동용
    path("logout", views.logout), #페이지 이동용
    path("logon_proc", views.logon_proc),  #로그온 처리
    path("logout_proc", views.logout_proc) #로그아웃처리 
]