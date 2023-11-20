
#Calculate Skewness, Kurtosis & draw inferences on the following data
 #     Cars speed and distance 
#Use Q9_a.csv

#SP and Weight(WT)
#Use Q9_b.csv


###----Cars speed and distance----####

import pandas as pd
df=pd.read_csv("Q9_a.csv")
df

df.describe()
list(df)
df.shape

df["speed"].hist()
df["speed"].skew()
df["speed"].kurt()


df["dist"].hist()
df["dist"].skew()
df["dist"].kurt()

df[['speed','dist']].hist()

df[['speed','dist']].skew()

df[['speed','dist']].kurtosis()