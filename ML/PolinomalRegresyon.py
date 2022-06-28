# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 16:12:28 2022

@author: Lenovo
"""

import numpy as np
import pandas as pd
import matplot.lib as plt


veri = pd.read_csv("Maaslar.csv")
print(veri)

#veri ön isleme

import sklearn.preprocessing as LabelEncoder

