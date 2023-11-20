# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 17:43:37 2023

@author: Durga Prasad
"""
import numpy as np
from scipy import stats
from scipy.stats import norm

## As z = (sample_mean-population-mean)/(standard deviation/sqrt(n))

##  1.96 = 5 /(40/sqrt(n))
## => 1.96 = 5 * sqrt(n)/40
## => sqrt(n) = (1.96*40)/5

n = ((1.96*40)/5)**2
n
round(n)

