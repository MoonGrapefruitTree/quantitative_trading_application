import quantitativeTradingBasics.initialize.database_init as database_init


test_stock_id = ['600028','601857','601668','601318','601390','601186','601628','601398','601939','600104']


test_data = database_init.get_testdata(test_stock_id)

test_data.to_csv('..\dictionary_file\\test_data.csv',encoding='utf-8')