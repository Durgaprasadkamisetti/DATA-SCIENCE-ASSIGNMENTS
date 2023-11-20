# -*- coding: utf-8 -*-
"""
Look at the data given below. Plot the data, find the outliers and find out  μ,σ,σ^2 ?
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

x=pd.Series([24.23,25.53,25.41,24.14,29.62,28.25,25.81,24.39,40.26,32.95,91.36,25.99,39.42,26.71,35])

#box plot
sns.boxplot(x)
#mean , standard deviation ,variance
x.mean()
x.std()
x.var()


