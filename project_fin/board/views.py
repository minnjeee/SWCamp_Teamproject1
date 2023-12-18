from django.shortcuts import render


# from board.models import Market

from django.db import connection
from common.CommonUtil import dictfetchall, CommonPage

def list(request, pg):
    cursor=connection.cursor()
    sql = "select count(*) from board_board"
    cursor.execute(sql)
    totalCnt = int(cursor.fetchone()[0])
    cp = CommonPage(totalCnt, pg, 10)

    sql= f"""
        select A.postnum, A.userid, A.username, A.title,
          to_char(A.wdate, 'yyyy-mm-dd') wdate, contents, hit, num 
        from 
        (   
            select postnum, userid, username, title, wdate, contents, hit,
            row_number() over(order by postnum desc) num,
            ceil (row_number() over(order by postnum desc)/10)-1 pg
            from board_board
        ) A
        where A.pg ={pg}
    
    """
    cursor.execute(sql)
    boardList=dictfetchall(cursor)
    # print(boardList)
    return render(request, "board/board_list.html", {'boardList':boardList, 'commonPage':cp})

from board.models import Board

def views(request, postnum):
    board = Board.objects.get(postnum = postnum)
    board.hit = board.hit+1
    board.save() 
    return render(request, "board/board_view.html", {'boardItem': board})

from board.forms import BoardForm

def write(request):
    return render(request, "board/board_write.html")

from django.utils import timezone
from django.shortcuts import redirect 
from django.db.models import Max

def save(request):
    form=BoardForm(request.POST)
    board=form.save(commit=False)
    b = len(Board.objects.all()) # 테이블에 저장된 데이터의 개수가
    if b == 0: # 0개이면
        board.postnum = 1 # 게시물번호 = 1
    else: # 아니면, 게시물번호 = 마지막 게시물번호 + 1
        max_score = Board.objects.aggregate(max_score=Max('postnum'))['max_score']
        board.postnum = max_score + 1
    board.wdate = timezone.now()
    board.hit=0
    board.save()

    return redirect("board:list", pg=0)

def modify(request, postnum):
    board = Board.objects.get(postnum = postnum)
    return render(request, "board/board_modify.html", {'boardItem': board})

def save2(request, postnum):
    form=BoardForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        board = Board.objects.get(postnum=postnum)
        board.username = cleaned_data['username']
        board.title = cleaned_data['title']
        board.contents = cleaned_data['contents']
        board.wdate = timezone.now()
        board.hit = 0
        board.save()
    return redirect("board:view", postnum=postnum)

def delete(request, postnum):
    board = Board.objects.get(postnum=postnum)
    board.delete()
    return redirect("board:list", pg=0)