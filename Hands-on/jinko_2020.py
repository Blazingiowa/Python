import pandas as pd
import math
import matplotlib.pyplot as plt
from sklearn.linear_model import  LinearRegression

df=pd.read_csv("jinko.csv",sep=',')
year=df.西暦.values.tolist()

year_list=[]
for i in year:
    year_list.append([i])

population=df.人口.values.tolist()

population_2020=[[2020]]

lr=LinearRegression(normalize=True)
lr.fit(year_list,population)
population_yosoku_2020=lr.predict(population_2020)
population_yosoku_2020=math.floor(population_yosoku_2020)
print('新潟県の2020年の予想人口は'+str(population_yosoku_2020)+'人と予想される')
df.plot(kind='bar', x='西暦', y='人口',rot=90,color='#4d5aaf')
plt.show()
