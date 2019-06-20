import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import  LinearRegression

nig=pd.read_csv('niigata.csv',skiprows=[9])
list_nig_x=[list(nig['1月']),list(nig['2月']),list(nig['3月']),list(nig['4月']),list(nig['5月']),list(nig['6月']),list(nig['7月']),list(nig['8月']),list(nig['9月']),list(nig['10月']),list(nig['11月'])]

nig_y=pd.read_csv('ansniigata.csv').values.tolist()

joetsu=pd.read_csv('niigata.csv')
sakata=joetsu.dropna()
murakami=list(sakata['12月'])

lr=LinearRegression(normalize=True)
lr.fit(list_nig_x,nig_y)
ar_predict_y=lr.predict(murakami)
print(ar_predict_y)
