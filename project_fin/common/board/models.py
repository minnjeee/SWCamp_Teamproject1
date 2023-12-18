from django.db import models

# Create your models here.

class Board(models.Model):
    postnum = models.IntegerField() # 등록번호
    userid=models.CharField(max_length=20) # 아이디
    username= models.CharField(max_length=20) # 이름
    title = models.CharField(max_length=100) # 제목
    wdate=models.DateTimeField() # 날짜
    contents=models.TextField() # 내용
    hit=models.IntegerField(default=0) # 조회수