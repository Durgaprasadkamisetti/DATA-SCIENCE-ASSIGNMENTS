# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 18:17:19 2023

@author: Durga Prasad
"""

#SP and Weight(WT)
#Use Q9_b.csv

import pandas as pd
df=pd.read_csv("Q9_b.csv")
df

list(df)
df.dtypes

df['SP'].hist()
df['SP'].skew()
df['SP'].kurtosis()


df['WT'].hist()
df['WT'].skew()
df['WT'].kurtosis()

df[['SP','WT']].hist()

df[['SP','WT']].skew()

df[['SP','WT']].kurtosis()
