# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:41:16 2020

@author: tugberk
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression

#Load the data
veriler = pd.read_csv("timeline.csv")

#eksik veriler
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
critical = veriler.iloc[:,11:12].values
imputer= imputer.fit(critical[::])
critical[::]=imputer.transform(critical[::])

total_Intubed = veriler.iloc[:,6:7].values
imputer = imputer.fit(total_Intubed[::])
total_Intubed[::] = imputer.transform(total_Intubed[::])

total_Intensive = veriler.iloc[:,7:8].values
imputer = imputer.fit(total_Intensive[::])
total_Intensive[::] = imputer.transform(total_Intensive[::])

for_intubed = veriler.iloc[:,:6].values

tests= veriler.iloc[:,8:9].values

son_veri = pd.DataFrame(data=for_intubed,index = range(203),columns=['case','totalcase','deaths','totalDeath','recoverd','totalRecovered'])
Intubed = pd.DataFrame(data=total_Intubed,index= range(203),columns=['Intubed'])
Intensive = pd.DataFrame(data=total_Intensive,index= range(203),columns=['Intensive'])
critical = pd.DataFrame(data=critical,index= range(203),columns=['critical'])


en_son = pd.concat([son_veri,Intubed],axis=1)
en_son2 = pd.concat([en_son,Intensive],axis=1)
en_son3 = pd.concat([en_son2,critical],axis=1)

# Ölümü tablodan ayırmak

cases = en_son3.iloc[:,:2]
after_death= en_son3.iloc[:,3:]
death = en_son3.iloc[:,2:3]

x = pd.DataFrame(data=cases,index=range(203),columns=['case','totalcase'])
y = pd.DataFrame(data=after_death,index=range(203),columns=['totalDeath','recoverd','totalRecovered','Intubed','Intensive','critical'])
DataDeath = pd.DataFrame(data=death,index = range(203),columns = ['deaths'])
z = pd.concat([x,y],axis=1)
son_veri = pd.concat ([z,DataDeath],axis=1)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(z,DataDeath,test_size=0.33,random_state=0)

regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)











