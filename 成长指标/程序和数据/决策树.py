# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 22:22:07 2020

@author: Hs
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import warnings
from matplotlib.axes._axes import _log as matplotlib_axes_logger
matplotlib_axes_logger.setLevel('ERROR')
plt.rcParams['font.sans-serif']=['SimHei']
warnings.filterwarnings("ignore")#忽略警示

def compare(x,y):
    w=0
    sum1=0
    for i in range(len(x)):
        sum1=sum1+1
        if x[i]==y[i]:
            w=w+1
    return w/sum1

data=pd.read_csv("tree_data.csv")
y = data['19']
X = data.drop(['1','2','3','4','5','6','7','8','9','12','19'], axis=1)
rate_test=np.zeros([1,10],float)
rate_train=np.zeros([1,10],float)
for i in range(0,10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=i, train_size=0.75)
    model_tree = DecisionTreeClassifier(criterion='entropy',max_depth=5)
    model_tree.fit(X_train, y_train)
    model_tree.predict(X_test)
    rate_test[0,i]=compare(y_test.values,model_tree.predict(X_test))
    rate_train[0,i]=compare(y_train.values,model_tree.predict(X_train))

print('')
print('十折交叉验证测试集准确率为：'+str(rate_test))
print('十折交叉验证测试集平均准确率为：'+str(sum(sum(rate_test))/10))
print('十折交叉验证训练集准确率为：'+str(rate_train))
print('十折交叉验证训练集平均准确率为：'+str(sum(sum(rate_train))/10))
'''
data = pd.read_csv("tree_data.csv")
y = data['19']
X = data.drop('19', axis=1)
data_feature_name = data.columns[0:18]
data_target_name =str( np.unique(y))
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=i, train_size=0.75)
model_tree.fit(X_train, y_train)

import pydotplus
from sklearn import tree
from IPython.display import Image
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.37/bin/'
dot_tree = tree.export_graphviz(model_tree,out_file=None,
                                feature_names=data_feature_name,
                                class_names=data_target_name,
                                filled=True,
                                rounded=True,
                                special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_tree)
img = Image(graph.create_png())
graph.write_png("out_depth.png")
'''