from django.shortcuts import render

# Create your views here.
from local.models import Market

from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse


srcs = [staticfiles_storage.url('img/서울시장1.jpg'),staticfiles_storage.url('img/서울시장2.jpg'),staticfiles_storage.url('img/서울시장3.jpg'),staticfiles_storage.url('img/서울시장4.jpg'),
        staticfiles_storage.url('img/경기시장1.jpg'),staticfiles_storage.url('img/경기시장2.jpg'),staticfiles_storage.url('img/경기시장3.jpg'),staticfiles_storage.url('img/경기시장4.jpg'),
        staticfiles_storage.url('img/강원시장1.jpg'),staticfiles_storage.url('img/강원시장2.jpg'),staticfiles_storage.url('img/강원시장3.jpg'),staticfiles_storage.url('img/강원시장4.jpg'),
        staticfiles_storage.url('img/충청시장1.jpg'),staticfiles_storage.url('img/충청시장2.jpg'),staticfiles_storage.url('img/충청시장3.jpg'),staticfiles_storage.url('img/충청시장4.jpg'),
        staticfiles_storage.url('img/전라시장1.jpg'),staticfiles_storage.url('img/전라시장2.jpg'),staticfiles_storage.url('img/전라시장3.jpg'),staticfiles_storage.url('img/전라시장4.jpg'),
        staticfiles_storage.url('img/경상시장1.jpg'),staticfiles_storage.url('img/경상시장2.jpg'),staticfiles_storage.url('img/경상시장3.jpg'),staticfiles_storage.url('img/경상시장4.jpg'),
        staticfiles_storage.url('img/제주시장1.jpg'),staticfiles_storage.url('img/제주시장2.jpg'),staticfiles_storage.url('img/제주시장3.jpg'),staticfiles_storage.url('img/제주시장4.jpg')
        ]

def server1(request):
    marketList = Market.objects.filter(region="서울")
    srcList = srcs[0:4]
    return render(request, 'local/local_server1.html',{'dataList':marketList, 'srcList':srcList})

def server2(request):
    marketList = Market.objects.filter(region="경기")
    srcList = srcs[4:8]
    return render(request, 'local/local_server2.html',{'dataList':marketList, 'srcList':srcList})

def server3(request):
    marketList = Market.objects.filter(region="강원")
    srcList = srcs[8:12]
    return render(request, 'local/local_server3.html',{'dataList':marketList, 'srcList':srcList})

def server4(request):
    marketList = Market.objects.filter(region="충청")
    srcList = srcs[12:16]
    return render(request, 'local/local_server4.html',{'dataList':marketList, 'srcList':srcList})

def server5(request):
    marketList = Market.objects.filter(region="전라")
    srcList = srcs[16:20]
    return render(request, 'local/local_server5.html',{'dataList':marketList, 'srcList':srcList})

def server6(request):
    marketList = Market.objects.filter(region="경상")
    srcList = srcs[20:24]
    return render(request, 'local/local_server6.html',{'dataList':marketList, 'srcList':srcList})

def server7(request):
    marketList = Market.objects.filter(region="제주")
    srcList = srcs[24:28]
    return render(request, 'local/local_server7.html',{'dataList':marketList, 'srcList':srcList})

def detail(request, id):
    market = Market.objects.get(id=id)
    image = srcs[id-1]
    return render(request, 'local/local_detail.html',{'data':market, 's':image})
