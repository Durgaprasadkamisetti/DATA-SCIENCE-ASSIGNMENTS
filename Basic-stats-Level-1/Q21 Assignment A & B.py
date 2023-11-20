# ## Q 21 Set A
"""
Check whether the data follows normal distribution
a)	Check whether the MPG of Cars follows Normal Distribution 
        Dataset: Cars.csv

"""

import pandas as pd
df = pd.read_csv('Cars.csv')
df

df.shape

df.info()

list(df)

df.describe()
df['MPG'].hist()

df['MPG'].skew()


##### Q 21 Set b
"""
b)	Check Whether the Adipose Tissue (AT) and Waist Circumference(Waist) 
     from wc-at data set  follows Normal Distribution 
       Dataset: wc-at.csv
"""

import pandas as pd
df=pd.read_csv('wc-at.csv')
df

df.info()

df.describe()

list(df)

df['Waist'].hist()

df['Waist'].skew()

df['AT'].hist()


df['AT'].skew()





