import pymysql
import pandas as pd

db = pymysql.connect(host='localhost',
                     user='qauser',
                     password='123456',
                     database='qadata',
                     charset='utf8')
cur = db.cursor()
# sql = "select * from comprehensive_Sdata LIMIT 10;"
sql = 'select COLUMN_NAME,COLUMN_COMMENT from information_schema.columns where TABLE_NAME=\'comprehensive_Sdata\''
cur.execute(sql)
indicator_dict = cur.fetchall()
cur.close()
db.close()
indicator_dict = pd.DataFrame(list(indicator_dict),columns=['COLUMN_NAME','COLUMN_COMMENT'])
# print(indicator_dict[indicator_dict.COLUMN_COMMENT=='前收盘价'].COLUMN_NAME)
indicator_dict.to_csv('..\dictionary_file\indicator_dict.csv',encoding='utf-8')
print(indicator_dict)