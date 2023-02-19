import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('IT Salary Survey EU 18-20.csv')
print(df.head())
print(df.isnull().sum())

df.dropna(inplace=True)
plt.hist(df['Salary'], bins=30)
plt.xlabel('Salary')
plt.ylabel('Count')
plt.show()

plt.scatter(df['Years of Experience'], df['Salary'])
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
sns.boxplot(x='Job Title', y='Salary', data=df)
plt.xticks(rotation=90)
plt.show()



