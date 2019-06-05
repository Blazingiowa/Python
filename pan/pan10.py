import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Testdata.csv')
df['合計']=df[['国語','数学','英語']].sum(axis=1)
df['順位']=df['合計'].rank(ascending=False)

color_list=['#474b42','#426579','#c97586','#4f455c','#008899','#dccb18','#302833','#839b5c','#f6b894','#007b43']
df.plot(kind='bar', x='ID', y='合計', color=color_list, rot=0)
plt.savefig('plot.png')
plt.show()

