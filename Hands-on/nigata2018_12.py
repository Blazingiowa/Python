import pandas as pd
from sklearn.linear_model import  LinearRegression
orig_shiwasu=5.9

nig=pd.read_csv('niigata.csv',skiprows=[9])
list_nig_x=[list(nig['1月']),list(nig['2月']),list(nig['3月']),list(nig['4月']),list(nig['5月']),list(nig['6月']),list(nig['7月']),list(nig['8月']),list(nig['9月']),list(nig['10月']),list(nig['11月'])]

nig_y=pd.read_csv('ansniigata.csv')
nig_y=list(nig_y['答'])

joetsu=pd.read_csv('niigata.csv')
nagaoka=joetsu.dropna()
murakami=[list(nagaoka['12月'])]

lr=LinearRegression(normalize=True)
lr.fit(list_nig_x,nig_y)
shiwasu=lr.predict(murakami)

keitei=orig_shiwasu-shiwasu
print('平成最後の12月の予想気温は'+str(shiwasu)+'℃です')
print('実際の平成最後の12月平均気温との逕庭は'+str(keitei)+'℃です')