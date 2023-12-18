from django.db import models

# Create your models here.

class Market(models.Model):
    market_name = models.CharField(max_length=50)   # 시장명
    market_type = models.CharField(max_length=20)   # 시장유형
    adres = models.CharField(max_length=100)        # 도로명주소
    region = models.CharField(max_length=10)        # 지역구분
    x = models.FloatField()                         # 위도
    y = models.FloatField()                         # 경도
    stores_num = models.IntegerField()              # 점포수
    items = models.CharField(max_length=100)        # 취급품목
    giftcard = models.CharField(max_length=100)     # 사용가능상품권
    toilet = models.CharField(max_length=10)        # 공중화장실보유여부
    parkinglot = models.CharField(max_length=10)    # 주차장보유여부