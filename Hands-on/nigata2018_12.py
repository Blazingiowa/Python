import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import  LinearRegression

nig=pd.read_csv('niigata.csv')
print(nig)
list_nig=list(nig['1月'])
print(list_nig)