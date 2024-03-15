import pandas
import numpy as np
from quantitativeTradingBasics.initialize.constants import risk_free_rate

##每天相比与前一天的增长率,以及相比于第一天的倍数
def get_pct_change(data,name):
    data = data[[name]].dropna(axis=0,how='any')
    data_yesterday = data.shift(1)
    daily_change = data/data_yesterday#每天相比与前一天的增长率
    daily_change_log = np.log(daily_change)
    pct_change = daily_change_log.cumsum().apply(np.exp)
    pct_change.columns = ['pct_change']
    return daily_change,pct_change

##每天相比与第一天的收益率
def get_yield(data,name):
    data = data[[name]].dropna(axis=0, how='any')
    data_buy = data[[name]].head(1).values[0]
    rate_yield = data[[name]]/data_buy-1
    rate_yield.columns =['yield']
    return rate_yield

##年化收益率
def get_annual_yield(data,name):
    rate_yield = get_yield(data,name)
    annual_yield = pow(rate_yield+1,250/len(rate_yield))-1
    annual_yield.columns = ['annual_yield']
    return annual_yield

##最大回撤
def get_max_pullback(data,name):
    data = data[[name]].dropna(axis=0, how='any')
    daily_pullback = (data[[name]].cummax()-data[[name]])/data[[name]].cummax()
    daily_pullback.columns = ['daily_pullback']
    max_pullback = daily_pullback.cummax()
    max_pullback.columns = ['max_pullback']
    return daily_pullback, max_pullback

#夏普比率
def get_sharpe_ratio(data,name,risk_free_rate = risk_free_rate):
    annual_yield = get_annual_yield(data, name)
    sharpe_ratio = (annual_yield.mean()-risk_free_rate)/annual_yield.std()
    sharpe_ratio.index = ['sharpe_ratio']
    return sharpe_ratio

def get_alpha():
    pass

def get_beta():
    pass