# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 13:31:40 2022

@author: Lenovo
"""

import numpy as np
import pandas as pd

data = pd.read_csv("weather.csv")
print(data)
#print(data.size)

#veri on isleme

#encoder islemi: kategorik->numeric
from sklearn.preprocessing import LabelEncoder
label_encoding = data.apply(LabelEncoder().fit_transform)



data2 = label_encoding.iloc[:,:5]

from sklearn import preprocessing 
one_hot_encoding = preprocessing.OneHotEncoder()
data2= one_hot_encoding.fit_transform(data2).toarray()