# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 11:10:28 2022

@author: Lenovo
"""

#1.kutuphaneler
import pandas as pd
import numpy as np

#2.veri onisleme
#2.1.veri yukleme
veriler = pd.read_csv('veriler.csv')
#pd.read_csv("veriler.csv")
#test
print(veriler)



#encoder: Kategorik -> Numeric
ulke = veriler.iloc[:,0:1].values
print(ulke)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

ulke[:,0] = le.fit_transform(veriler.iloc[:,0])

print(ulke)


ohe = preprocessing.OneHotEncoder()
ulke = ohe.fit_transform(ulke).toarray()
print(ulke)



#encoder: Kategorik -> Numeric
c = veriler.iloc[:,-1:].values
print(c)


le = preprocessing.LabelEncoder()

c[:,-1] = le.fit_transform(veriler.iloc[:,-1])

print(c)


ohe = preprocessing.OneHotEncoder()
c = ohe.fit_transform(c).toarray()
print(c)


#numpy dizileri dataframe donusumu
sonuc = pd.DataFrame(data=ulke, index = range(22), columns = ['fr','tr','us'])
print(sonuc)

sonuc2 = pd.DataFrame(data=veriler, index = range(22), columns = ['boy','kilo','yas'])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3 = pd.DataFrame(data = c[:,:1], index = range(22), columns = ['cinsiyet'])
print(sonuc3)
#data = c[:,:1] bu tanımlama ile dummy trap i onlemis oluyoruz, erkek/kadın iki kolonu degilde tek kolonu alıcak

#dataframe birlestirme islemi
s=pd.concat([sonuc,sonuc2], axis=1)
print(s)

s2=pd.concat([s,sonuc3], axis=1)
print(s2)

#verilerin egitim ve test icin bolunmesi
from sklearn.model_selection import train_test_split

x_train, x_test,y_train,y_test = train_test_split(s,sonuc3,test_size=0.33, random_state=0)

# Regrasyon Uygulanması
#model insasi
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train) 

y_pred = regressor.predict(x_test)

print(y_pred)

boy = s2.iloc[:,3:4].values
print(boy)

sol = s2.iloc[:,:3]
sag = s2.iloc[:,4:]

veri = pd.concat([sol,sag],axis=1)

x_train, x_test,y_train,y_test = train_test_split(veri,boy,test_size=0.33, random_state=0)

regressor2 = LinearRegression()
regressor2.fit(x_train,y_train) 

y_pred = regressor2.predict(x_test)
