# -*- coding: utf-8 -*-
"""
Created on Sat May  9 13:58:09 2020

@author: Hs
"""
import numpy as np
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()

data=np.loadtxt('data.csv',delimiter=',')
std_data=ss.fit_transform(data)
#np.savetxt('std_data.csv', std_data, delimiter = ',')
#std_data=np.delete(std_data,12,axis=1)
p=np.loadtxt('主成分.csv',delimiter=',')
c=np.loadtxt('得分系数.csv',delimiter=',')
Principal=np.dot(std_data,p)
c=c/sum(c)
score=np.dot(Principal,c)
#np.savetxt('score.csv', score, delimiter = ',')

fenweidian=np.loadtxt('得分分位点.csv',delimiter=',')#根据根据得分将企业划分为10份
kind=np.zeros([score.shape[0],1],'float')#按照得分划分为10类
for i in range(kind.shape[0]):
    for j in range(0,fenweidian.shape[0]):
        if j==0:
            if score[i]<=fenweidian[j]:
                kind[i,0]=j+1
                break
        else :
            if score[i]>fenweidian[j-1] and score[i]<=fenweidian[j]:
                kind[i,0]=j+1
                break
            else :
                kind[i,0]=j+2
#np.savetxt('kind.csv', kind, delimiter = ',')
