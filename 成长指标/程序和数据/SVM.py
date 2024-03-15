# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:53:55 2020

@author: Hs
"""

from sklearn import svm
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import warnings
from matplotlib.axes._axes import _log as matplotlib_axes_logger

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
for c in [100]:
    for G in [0.1]:
        for i in range(0,10):#十折交叉验证
            X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=i, train_size=0.90)
            clf = svm.SVC(kernel='rbf',C=c,gamma=G)
            clf.fit(X_train, y_train.ravel())
            rate_test[0,i]=compare(y_test.T,clf.predict(X_test))
            rate_train[0,i]=compare(y_train.T,clf.predict(X_train))
        print('')
        print(c,G)
        print('十折交叉验证测试集准确率为：'+str(rate_test))
        print('十折交叉验证测试集平均准确率为：'+str(sum(sum(rate_test))/10))
        print('十折交叉验证训练集准确率为：'+str(rate_train))
        print('十折交叉验证训练集平均准确率为：'+str(sum(sum(rate_train))/10))
    
    
    
    