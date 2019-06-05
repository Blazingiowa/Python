import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Testdata.csv')
df['合計']=df[['国語','数学','英語']].sum(axis=1)
df['順位']=df['合計'].rank(ascending=False)

df.plot(kind='bar', x='ID', y='合計', rot=90)
plt.show()