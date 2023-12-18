import pandas as pd

# 데이터 가공 부분

data = pd.read_csv('전국전통시장표준데이터.csv')

print(data.columns)
# ['시장명', '시장유형', '소재지도로명주소', '소재지지번주소', '시장개설주기', '위도', '경도', '점포수',        
#        '취급품목', '사용가능상품권', '홈페이지주소', '공중화장실보유여부', '주차장보유여부', '개설연도', '전화번호',
#        '데이터기준일자', '제공기관코드', '제공기관명']

print(data['시장유형'].value_counts(dropna=False)) # 상설장, 상설장+5일장, 5일장, 상설장+3일장 ('상설+오일장'데이터(1개)를 '상설장+5일장'으로, '상설'데이터(1개)를 '상설장'으로)
print(data['취급품목'].value_counts(dropna=False)) # 분리해서 저장할 방법을 생각해보자
print(data['홈페이지주소'].value_counts(dropna=False)) # 해당사항없음, 없음 항목 있음 (+ 결측치 1418개)
print(data['공중화장실보유여부'].value_counts(dropna=False))
print(data['주차장보유여부'].value_counts(dropna=False))
print(data['개설연도'].value_counts(dropna=False))
print(data['개설연도'].unique()) # 1935-12-15' '1929-03-02' '1921-10-07' '1929-09-02' -> 연도-월-일 형태로 저장된 데이터 있음 (나머지는 연도만 저장)
                                # nan 데이터 존재


for index, row in data.iterrows():
    if row['시장유형'] == '상설+오일장':
        data.loc[index, '시장유형'] = '상설장+5일장'
    elif row['시장유형'] == '상설':
        data.loc[index, '시장유형'] = '상설장'

    # if (row['홈페이지주소'] == '해당사항없음') or (row['홈페이지주소'] == '없음'):
    #     data.loc[index, '홈페이지주소'] = ""

    # 개설연도 = str(row['개설연도'])
    # if '-' in 개설연도 :
    #     개설연도 = 개설연도.split('-')[0]
    #     data.loc[index,'개설연도'] = 개설연도

    취급품목 = str(row['취급품목'])
    data.loc[index, '취급품목'] = 취급품목.replace('+',',')

    사용가능상품권 = str(row['사용가능상품권'])
    data.loc[index,'사용가능상품권'] = 사용가능상품권.replace('+',',')

    도로명주소 = str(row['소재지도로명주소'])
    data.loc[index,'지역구분'] = 도로명주소.split(' ')[0]
    
for index, row in data.iterrows():    
    if (row['지역구분'] == '인천광역시') or (row['지역구분'] =='화성시') or (row['지역구분']=='경기도'):
        data.loc[index,'지역구분'] = '경기'
    elif row['지역구분'] == '서울특별시':
        data.loc[index,'지역구분'] = '서울'
    elif row['지역구분'] == '강원도':
        data.loc[index,'지역구분'] = '강원'
    elif (row['지역구분'] == '충청북도') or (row['지역구분'] =='충청남도') or (row['지역구분'] =='대전광역시') or (row['지역구분'] =='세종특별자치시'):
        data.loc[index,'지역구분'] = '충청'
    elif (row['지역구분'] == '광주광역시') or (row['지역구분'] =='전라남도') or (row['지역구분'] =='전라북도'):
        data.loc[index,'지역구분'] = '전라'
    elif (row['지역구분'] == '부산광역시') or (row['지역구분'] =='대구광역시') or (row['지역구분'] =='울산광역시') or (row['지역구분'] =='경상남도') or (row['지역구분'] =='경상북도'):
        data.loc[index,'지역구분'] = '경상'
    elif row['지역구분'] == '제주특별자치도':
        data.loc[index,'지역구분'] = '제주'


print(data['지역구분'].unique())



data = data.replace({pd.NA: None}) # nan값을 none으로 변경

data = data[['시장명','시장유형','소재지도로명주소', '지역구분','위도','경도','점포수','취급품목','사용가능상품권','공중화장실보유여부','주차장보유여부']]

data.to_csv('data.csv', index=False)


####################################################################################################

# 데이터 선택 부분 (첫번째 기준: 온누리상품권 사용가능한 시장, 두번째 기준: 점포수가 많은 시장)

data = pd.read_csv('data.csv')

for index, row in data.iterrows():
    상품권 = str(row['사용가능상품권'])
    if '온누리상품권' in 상품권:
        data.loc[index, '표시'] = 1

data2 = data[data['표시'] == 1]
print(len(data2)) # 온누리상품권이 사용가능한 전지역 시장 수 =94
print(len(data2[data2['지역구분']=='서울'])) #4
print(len(data2[data2['지역구분']=='경기'])) #18
print(len(data2[data2['지역구분']=='강원'])) #7
print(len(data2[data2['지역구분']=='충청'])) #0
print(len(data2[data2['지역구분']=='전라'])) #16
print(len(data2[data2['지역구분']=='경상'])) #48
print(len(data2[data2['지역구분']=='제주'])) #0

d1 = data[data['지역구분']=='서울']
d2 = data[data['지역구분']=='경기']
d3 = data[data['지역구분']=='강원']
d4 = data[data['지역구분']=='충청']
d5 = data[data['지역구분']=='전라']
d6 = data[data['지역구분']=='경상']
d7 = data[data['지역구분']=='제주']

# d1 = d1.sort_values(by="점포수", ascending=False)
# print(d1[0:4])

df2 = pd.DataFrame()

for df in [d1,d2,d3,d4,d5,d6,d7]:
    if len(df[df['표시']==1]) == 0:
        df = df.sort_values(by="점포수", ascending=False)
        df = df[0:4]
    else:
        df = df[df['표시']==1]
        df.sort_values(by='점포수', ascending=False)[0:4]
        df = df[0:4]
    df2 = pd.concat([df2,df], axis=0)

print(len(df2))
df2 = df2[['시장명','시장유형','소재지도로명주소', '지역구분','위도','경도','점포수','취급품목','사용가능상품권','공중화장실보유여부','주차장보유여부']]
print(df2)

df2.to_csv('data2.csv', index=False)