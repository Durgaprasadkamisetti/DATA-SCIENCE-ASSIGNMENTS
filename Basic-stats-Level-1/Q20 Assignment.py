# -*- coding: utf-8 -*- Assignment Q20
"""
Calculate probability from the given dataset for the below cases

Data _set: Cars.csv
Calculate the probability of MPG  of Cars for the below cases.
       MPG <- Cars$MPG
a.	P(MPG>38)
b.	P(MPG<40)
c.  P (20<MPG<50)

"""
from scipy.stats import norm
import pandas as pd
df = pd.read_csv('Cars.csv')
df
mpg = df['MPG']

# a. P(MPG > 38)
prob_a = 1 - norm.cdf(38, loc=mpg.mean(), scale=mpg.std())
prob_a
# b. P(MPG < 40)
prob_b = norm.cdf(40, loc=mpg.mean(), scale=mpg.std())
prob_b
# c. P(20 < MPG < 50)
prob_c = norm.cdf(50, loc=mpg.mean(), scale=mpg.std()) - norm.cdf(20, loc=mpg.mean(), scale=mpg.std())
prob_c
