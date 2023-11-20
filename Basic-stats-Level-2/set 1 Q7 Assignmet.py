import pandas as pd
df=pd.read_csv("Q7.csv")
df
list(df)

df.describe()

df["Points"].var()

df["Points"].median()

df["Points"].mode()

df["Score"].var()

df["Score"].median()

df["Score"].mode()

df["Weigh"].var()

df["Weigh"].median()

df["Weigh"].mode()

df.isna().sum()

df["Score"].value_counts()

df["Weigh"].hist()

df["Weigh"].skew()

df["Points"].hist()

df["Points"].skew()

df["Score"].hist()

df["Score"].skew()

import seaborn as sns
import matplotlib.pyplot as plt

sns.lineplot(x='Points', y='Score', data=df)
plt.show()

sns.countplot(x='Weigh', data=df)
plt.show()

sns.heatmap(df.corr(), annot=True, cmap='viridis')
plt.show()

sns.violinplot(x='Score', y='Weigh', data=df)
plt.show()

sns.heatmap(df.corr(), annot=True, cmap='cividis')
plt.show()

sns.heatmap(df.corr(), annot=True, cmap='plasma')
plt.show()

sns.heatmap(df.corr(), annot=True, cmap='inferno')
plt.show()





