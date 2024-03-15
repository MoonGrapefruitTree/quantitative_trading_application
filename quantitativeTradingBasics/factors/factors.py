import pandas

#七日均线
def mean7(data,name):
    test_data = data[[name]].dropna(axis=0,how='any')

    mean7=test_data.rolling(window=7).mean()
    return mean7

#自定义均线
def mean_all(data,name,num):
    test_data = data[[name]].dropna(axis=0, how='any')
    mean_all=test_data.rolling(window=num).mean()
    return mean_all

def PBR(data,name_Clpr='Clpr',name_NAPS='NAPS'):
    data['PBR'] = data[name_Clpr]/data[name_NAPS]
    return data