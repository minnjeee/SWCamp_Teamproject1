import cx_Oracle
from django.db import connection


def dictfetchall(cursor):
    
    columns = [ col[0].lower() for col in cursor.description]
    #print( columns  )
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


# << < 1 2 3 4 5 6 7 8 9 10 > >> 
# << : 첫번째 페이지, 항상 
# < : 현재 페이지로부터 앞으로 이동할 페이지가 있는 지 현재 9 이전 < 8페이지 
# 1,2,,3...10 첫번째 그룹 : 1 ~ 10   현재 : 4   1번 그룹
#             두번째 그룹 : 11 ~ 20  현재 : 12  2번 그룹
#             세번째 그룹 : 21 ~ 30  현재 : 29  3번 그룹

# > : 현재 페이지로부터 앞으로 이동할 페이지가 있는 지 현재 9 다음 > 10페이지 
# >> 마지막 페이지 

import math
class CommonPage: 
    #페이징에 필요한 3가지 정보 (전체 개수, 한 페이지에 표시될 개수, 현재 페이지)
    #totalCnt : 전체 데이터 개수 
    #pageSize : 한 페이지에 데이터를 몇 건씩 보여줄거야 
    #전체 페이지 개수 : ceil(totalCnt / pageSize) 
    # 232/10 - 23.2 - 올림- 24페이지 
    #curPage : 현재페이지 
    #파이썬에 클래스를 설계할 때 가급적 생성자에서 변수를 만드는 게 낫다 
    def __init__(self, totalCnt=1, curPage=0, pageSize=10):
        self.curPage = curPage
        self.totalCnt = totalCnt
        self.totalPage = math.ceil(totalCnt/pageSize)-1
        self.start= (curPage//pageSize)*10 #그룹시작 
        self.end= self.start+10 #그룹종료
        if self.end > self.totalPage :
            self.end = self.totalPage+1 

        #3 0 10 
        #12 10 20
        #32 30 40

        if self.curPage >= 1: #앞으로 이동 가능 
            self.isPrev=True
            self.prev_page=self.curPage-1 
        else : #더 이상 앞으로 갈 수 없음 
            self.isPrev=False
            self.prev_page=0

        if self.curPage <= self.totalPage: #뒤쪽으로 이동가능
            self.isNext=True
            self.next_page=self.curPage+1 
        else : #더 이상 앞으로 갈 수 없음 
            self.isNext=False
            self.next_page=self.curPage

        self.page_range= range(self.start, self.end)

