# -*- coding: utf-8 -*-
"""
Calculate probability from the given dataset for the below cases

Data _set: Cars.csv
Calculate the probability of MPG  of Cars for the below cases.
       MPG <- Cars $MPG
a.	P(MPG>38)
b.	P(MPG<40)
c.  P (20<MPG<50)

"""
from scipy import stats
from scipy.stats import norm
import pandas as pd
df=pd.read_csv('Cars.csv')
df

list(df)

len(df)
df.describe()

df.info()


# a. P(MPG > 38)
1-stats.norm.cdf(38,df.MPG.mean(),df.MPG.std())

# b. P(MPG < 40)
stats.norm.cdf(40,df.MPG.mean(),df.MPG.std())

# c. P(20 < MPG < 50)
stats.norm.cdf(0.50,df.MPG.mean(),df.MPG.std())-stats.norm.cdf(0.20,df.MPG.mean(),df.MPG.std())
