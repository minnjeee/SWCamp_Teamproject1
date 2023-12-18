from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from member.models import Member 

def write(request):
    return render(request, "member\member_write.html")

def logon(request):
    return render(request, "member\logon.html")

def logout(request):
    return render(request, "member\logout.html")

from member.forms import MemberForm
from django.utils import timezone
def save(request):
    try:
        memberForm = MemberForm(request.POST)
        member = memberForm.save(commit=False) 
        member.wdate = timezone.now()
        member.save()
        result = {"result":"success"}
    except Exception as ex:
        print(ex)
        result = {"result":"fail"}

    return JsonResponse(result)

def logon_proc(request):
    result = {"result":"OK"}
    return JsonResponse(result)

def logout_proc(request):
    result = {"result":"OK"}
    return JsonResponse(result)

def idcheck(request):
    userid = request.POST.get("userid")
    print(userid)
    #디비에가서 확인 
    try:
        Member.objects.get(userid=userid) #이미 사용중인 아이디임 사용못함
        result = {"result":"fail"}
    except:
        result = {"result":"success"} #아이디 안쓰고 있음 사용가능 
    return JsonResponse(result)
"""
insert into member_member(id, userid, password, username, email, phone, wdate)
values(1, 'test', '1234', '홍길동', 'hong@hanmail.net', '010-0000-0000', sysdate);
commit;
"""
