import pymysql
import pandas as pd

def get_testdata(Stkcd_id=['000001']):
    qadata = pymysql.connect(host='localhost',
                     user='qauser',
                     password='123456',
                     database='qadata',
                     charset='utf8')
    qa_cursor = qadata.cursor()
    for i in Stkcd_id:
        strs = '\''+str(i)+'\'' +' , '
    strs = 'Stkcd in (' +strs[0:-3]+') '
    sql = 'select * from comprehensive_Sdata where '+strs+' order by \'Date\';'
    qa_cursor.execute(sql)
    test_data = qa_cursor.fetchall()
    column_names = []
    col_names = qa_cursor.description
    for col_name in col_names:
        column_names.append(col_name[0])
    qa_cursor.close()
    qa_cursor.close()
    testdata = pd.DataFrame(test_data,columns=column_names)
    testdata.set_index('Date',inplace=True)
    return testdata