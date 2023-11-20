# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 11:47:22 2023

@author: Durga Prasad
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import binom

n=5
p=1/200
Bi=binom(n=5,p=1/200)
#p(x<1)
p=1-Bi.cdf(0)
p
