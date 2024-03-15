import pandas as pd
import numpy as np
import quantitativeTradingBasics.factors.factors as factors
import matplotlib
import matplotlib.pyplot as plt
import quantitativeTradingBasics.factors.indicators as indicators
matplotlib.use('TkAgg')     # 设置matplotlib的GUI后端

#金叉进，死叉出，双均线。data：数据 ，name：谁的均值，num1：均线日期(一般小)，num2：均线日期（一般大） 。
def gold_and_dead_fork(data, name, num1, num2,is_visualization=False):
    data = data[[name]].dropna().dropna(axis=0,how='any')
    # num1 = min([num_1, num_2])
    # num2 = max([num_1, num_2])
    # num1 = num_1
    # num2 = num_2
    mean1 = factors.mean_all(data, name, num1)
    mean2 = factors.mean_all(data, name, num2)
    name_mean1 = 'mean'+str(num1)
    name_mean2 = 'mean' + str(num2)
    data[name_mean1] = mean1
    data[name_mean2] = mean2
    data['positions'] = np.where(data[name_mean1] > data[name_mean2], 1, -1)
    if is_visualization:
        data[['Clpr', name_mean1, name_mean2, 'positions']].plot(secondary_y='positions')
        plt.show()
    gd_data_pct_change = data[data['positions']==1]
    daily_change,gd_pct_change = indicators.get_pct_change(gd_data_pct_change,'Clpr')
    return data,gd_pct_change

##双均线 自动选择收益最高的两条均线
def gold_and_dead_fork_adaptive_parameter(data, name, num_1=[5, 10, 30], num_2=[60, 90, 180]):
    result=[]
    gdap_gd_pct_change=pd.DataFrame()
    for num1 in num_1:
        for num2 in num_2:
            if num1!=num2:
                data, gd_pct_change = gold_and_dead_fork(data, name, num1, num2)
                result.append([num1,num2,gd_pct_change['pct_change'].tail(1).values[0]])
                gdap_gd_pct_change[str(num1)+':'+str(num2)] = gd_pct_change
            else:
                result.append([num1, num2, 1])
                gdap_gd_pct_change[str(num1) + ':' + str(num2)] = 1
    result = pd.DataFrame(result)
    result.columns = ['days1','days2','pct_change']
    return result, gdap_gd_pct_change


