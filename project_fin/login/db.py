import cx_Oracle
import pandas as pd

conn = cx_Oracle.connect('user03/1234@127.0.0.1:1521/XE') # 데이터베이스에 연결

cursor = conn.cursor()

data = pd.read_csv('./data2.csv')

print(data.info())
data = data.replace({pd.NA: None})
#pd.set_option('display.max_rows', None)  # 모든 행 출력
#pd.set_option('display.max_columns', None)  # 모든 열 출력


for index, row in data.iterrows():

    t = (row['시장명'],row['시장유형'],row['소재지도로명주소'],row['지역구분'],
        row['위도'],row['경도'],row['점포수'],row['취급품목'],row['사용가능상품권'],
        row['공중화장실보유여부'],row['주차장보유여부'])
    sql = """
    insert into local_market(market_name, market_type, adres, region, x, y, stores_num, items, giftcard, toilet, parkinglot)
    values (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10, :11)
    """
    cursor.execute(sql, t)

conn.commit()

cursor.close()
conn.close()