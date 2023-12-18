from django import forms

#모델클래스를 import 해야한다 
#from 폴더명. 파일명 import 클래스명
from member.models import Member

class MemberForm(forms.ModelForm):
    class Meta:
        model= Member
        fields=['userid', 'username', 'password', 'email', 'phone']
        labels={'userid': '아이디',
                 'username': '이름',
                 'password':'패스워드',
                 'email':'이메일', 
                 'phone': '전화번호'}