import pandas as pd
df=pd.read_csv("Q7.csv")
df
list(df)

df.describe()

#--Points---##
df["Points"].mean()

df["Points"].median()

df["Points"].mode()

df["Points"].var()

df["Points"].std()

df["Points"].min()

df["Points"].max()
#range
df["Points"].max()-df["Points"].min()

##----Score--###
df["Score"].mean()

df["Score"].median()

df["Score"].mode()

df["Score"].var()

df["Score"].std()

df["Score"].min()

df["Score"].max()
#range
df["Score"].max()-df["Score"].min()

#--Weigh--##
df["Weigh"].mean()

df["Weigh"].median()

df["Weigh"].mode()

df["Weigh"].var()

df["Weigh"].std()

df["Weigh"].min()

df["Weigh"].max()
#range
df["Weigh"].max()-df["Weigh"].min()



