# -*- coding: utf-8 -*-
"""
2.	The current age (in years) of 400 clerical employees at an insurance 
claims processing center is normally distributed with mean  = 38 and
 Standard deviation  =6. For each statement below, please specify 
 True/False. If false, briefly explain why.
A.More employees at the processing center are older than 44 than between 38 and 44.
B.	A training program for employees under the age of 30 at the center would 
be expected to attract about 36 employees.

"""

from scipy import stats
from scipy.stats import norm

# (p>44)
y=1-stats.norm.cdf(44,loc=38,scale=6)
y
# p(38<x<44)
z=stats.norm.cdf(44,38,6)-stats.norm.cdf(38,38,6)
z
#(p<30)
z1=stats.norm.cdf(30,38,6)
z1
# N*P(x<30)
z2=400*stats.norm.cdf(30,38,6)
z2
