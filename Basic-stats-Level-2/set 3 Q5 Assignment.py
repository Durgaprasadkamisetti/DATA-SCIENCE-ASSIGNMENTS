# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 12:00:48 2023

@author: Durga Prasad
"""

import numpy as np
from scipy import stats

z=(0.046-0.05)/(np.sqrt(0.05*(1-0.05))/2000)
z
pvalue=1-stats.norm.cdf(abs(z))
pvalue
