# -*- coding: utf-8 -*-
"""
Created on Sat Jun 25 19:56:21 2022

@author: Lenovo
"""

# bolum 2: veri on isleme(data preprocessing)

#kutuphaneler
import pandas as pd # verileri duzgun bir sekilde tutmak, dataframe(vericerceveleri) olusturabilmek ve buradaki verilere duzgun bir sekilde ulasabilmek icin kullanılan kutuphane
import numpy as np #buyuk sayilar ve hesaplama islemleri icin kullandigimiz kutuphane
import matplotlib.pyplot as pltü # genelde gorsellestirme için kullanilan kutuphane

#kodlar

#veri yukleme
veriler= pd.read_csv('veriler.csv')
print(veriler)

#veri on isleme
boy = veriler[['boy']]
print(boy)

boykilo = veriler[['boy', 'kilo']]
print(boykilo)

#python temelleri
class insan:
    boy = 180
    def kosmak(self, b):
        return b + 10
    
ali = insan()
print(ali.boy)
print(ali.kosmak(90))

liste = [1,2,3]
print(liste)

#eksik veriler

eksikveriler= pd.read_csv('eksikveriler.csv')
print(eksikveriler)

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

yas = eksikveriler.iloc[:,1:4].values
print(yas)
imputer = imputer.fit(yas[:,1:4])
yas[:,1:4] = imputer.transform(yas[:,1:4])
print(yas)

#kategorik veri donusumu
# encoder: kategorik(nominal,ordinal)->>numeric
ulke = veriler.iloc[:,0:1].values
print(ulke)

from sklearn import preprocessing

label_encoding = preprocessing.LabelEncoder() # sayısal olarak herbir değere 0,1,2,3,4,5,... gibi degerler verir

ulke[:,0] = label_encoding.fit_transform(veriler.iloc[:,0])
print(ulke)

one_hot_encoding = preprocessing.OneHotEncoder() # kolon baslıklarına etiketleri tasımak ve her bir etiketin altına 1 veya 0 (oraya ait/degil) yazmak
ulke = one_hot_encoding.fit_transform(ulke).toarray()
print(ulke)

# numpy dizilerinin dataframee donusumu

print(list(range(22)))
sonuc = pd.DataFrame(data = ulke, index = range(22), columns = ['fr', 'tr', 'us'])
print(sonuc)

sonuc2 = pd.DataFrame(data = yas, index = range(22), columns =  ['boy', 'kilo', 'yas'])
print(sonuc2)

cinsiyet = veriler.iloc[:,-1].values
print(cinsiyet)

sonuc3 = pd.DataFrame(data = cinsiyet, index = range(22), columns =  ['cinsiyet'])
print(sonuc3)

# dataframe birlestirme islemi
s = pd.concat([sonuc,sonuc2], axis = 1) #axis parametresi ile altalta degilde yanyan ekleme saglar
print(s)

s2 = pd.concat([s,sonuc3], axis = 1) #axis=1 ile satır baslıklarından esitler, 1.colums a bakar
print(s2)

#verinin train(egitim) ve test olarak bolunmesi islemi

from sklearn.model_selection import train_test_split
#veri train,test,bagimli degisken,bagimsiz degisken olarak 4 parcaya, 2 farklı boyutta bolunur

x_train, x_test, y_train, y_test = train_test_split(s, sonuc3, test_size = 0.33, random_state = 0)

# verinin öznitelik olcekleme islemi

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

X_train = sc.fit_transform(x_train)
X_test = sc.fit_transform(x_test)