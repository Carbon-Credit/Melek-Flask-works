# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 19:27:57 2022

@author: Lenovo
"""

#kutuphaneler
import numpy as np
import pandas as pd

#veri yukleme
datas = pd.read_csv("odev_tenis.csv")
print(datas)

#veri on isleme

#encoder islemi: kategorik->numeric
from sklearn.preprocessing import LabelEncoder
datas2 = datas.apply(LabelEncoder().fit_transform)

from sklearn import preprocessing 
ohe = preprocessing.OneHotEncoder()
datas3 = datas2.iloc[:,:1]
datas3 = ohe.fit_transform(datas3).toarray()
#print(datas3)


havadurumu = pd.DataFrame(data=datas3, index=range(14), columns = ['overcast','rainy','sunny'])

sonveriler = pd.concat([havadurumu,datas.iloc[:,1:3]], axis = 1)
sonveriler = pd.concat([datas2.iloc[:,-2:],sonveriler],axis = 1)

#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split
x_train, x_test,y_train,y_test = train_test_split(sonveriler.iloc[:,:-1],sonveriler.iloc[:,-1:],test_size=0.33, random_state=0)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)


y_pred = regressor.predict(x_test)

print(y_pred)

#modelin ve modeldeki degişkenlerin başarısı ile ilgili bir sistem kurmak için eklenen kütüphane
import statsmodels.api as sm

X = np.append(arr = np.ones((14,1)).astype(int), values=sonveriler.iloc[:,:-1], axis=1 ) #bu işlemle doğrusal denkleme sabit değişken olarak 1 i dikey olarak ekledik

X_l = sonveriler.iloc[:,[0,1,2,3,4,5]].values#tum satır ve kolonları aldık
X_l = np.array(X_l, dtype = float) #bir dizi oluşturup değişkenleri sisteme ekleme
model = sm.OLS(sonveriler.iloc[:,-1:], X_l).fit()

print(model.summary())

sonveriler = sonveriler.iloc[:,1:]

X = np.append(arr = np.ones((14,1)).astype(int), values=sonveriler.iloc[:,:-1], axis=1 )

X_l = sonveriler.iloc[:,[0,1,2,3,4]].values
X_l = np.array(X_l, dtype = float) 
model = sm.OLS(sonveriler.iloc[:,-1:], X_l).fit()

print(model.summary())

x_train = x_train.iloc[:,1:]
x_test = x_test.iloc[:,1:]

regressor.fit(x_train,y_train)


y_pred = regressor.predict(x_test)
