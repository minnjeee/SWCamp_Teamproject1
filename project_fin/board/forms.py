from django import forms

from board.models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model= Board 
        fields=['title', 'username', 'contents']
        labels={'title':'제목', 'usrname':'작성자', 'contents':'내용'}