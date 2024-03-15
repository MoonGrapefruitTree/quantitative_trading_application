import numpy as np
from statsmodels import regression
import statsmodels.api as sm
#分位数去极值
def filter_extreme_percent(series,min=0.25,max=0.75):
    series_sort = series.sort_values()
    q = series_sort.quantile([min,max])
    return np.clip(series,q.iloc[0],q.iloc[1])


# mad去极值
def filter_extreme_mad(series,n=1):
    series = series.sort_values()
    madian = series.quantile(0.5)
    mad = (series - madian).abs().quantile(0.5)
    max_point = madian + n*mad
    min_point = madian - n*mad
    return np.clip(series,min_point,max_point)

#方差去极值
def filter_extreme_sigma(series,n=3):
    mean = series.mean()
    sigma = series.std()
    min_point = mean - n*sigma
    max_point = mean + n * sigma
    return np.clip(series,min_point,max_point)


#标准化
def standardize(series):
    return (series-series.mean())/series.std()

#中性化
def neutralize(series_y,series_x):
    result = sm.OLS(series_y.astype(float),series_x.astype(float)).fit()
    return result.resid