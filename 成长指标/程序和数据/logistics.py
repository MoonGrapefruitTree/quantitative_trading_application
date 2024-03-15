# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:01:24 2020

@author: Hs
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import matplotlib.pyplot as plt
from matplotlib.axes._axes import _log as matplotlib_axes_logger
matplotlib_axes_logger.setLevel('ERROR')
plt.rcParams['font.sans-serif']=['SimHei']

def compare(x,y):
    w=0
    sum1=0
    for i in range(len(x)):
        sum1=sum1+1
        if x[i]==y[i]:
            w=w+1
    return w/sum1
            
matplotlib_axes_logger.setLevel('ERROR')
plt.rcParams['font.sans-serif']=['SimHei']
warnings.filterwarnings("ignore")#忽略警示

X=np.loadtxt('std_data.csv',delimiter=',')
X=np.delete(X,[0,1,2,3,4,5,6,7,8,11],axis=1)
y=np.loadtxt('kind.csv',delimiter=',')
rate_test=np.zeros([1,10],float)
rate_train=np.zeros([1,10],float)
w=np.zeros([10,X.shape[1]],float)
for i in range(0,10):#十折交叉验证
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=i, train_size=0.90)
    clf = LogisticRegression()
    clf.fit(X_train, y_train.ravel())
    rate_test[0,i]=compare(y_test.T,clf.predict(X_test))
    rate_train[0,i]=compare(y_train.T,clf.predict(X_train))
    w[i,:]=sum(clf.coef_)
print('')
print('W='+str(w*(pow(10,13)))+'/10^13')
print('W='+str(sum(w*(pow(10,13))))+'/10^13')
print('十折交叉验证测试集准确率为：'+str(rate_test))
print('十折交叉验证测试集平均准确率为：'+str(sum(sum(rate_test))/10))
print('十折交叉验证训练集准确率为：'+str(rate_train))
print('十折交叉验证训练集平均准确率为：'+str(sum(sum(rate_train))/10))









