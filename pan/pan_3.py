#LEVEL3
import pandas as pd

df_list = pd.DataFrame([['1','2','3'],['4','5','6'],['7','8','9']],columns=['a','b','c'])
df_list['d']=(['x','y','z'])
df_list2 = pd.DataFrame([['10','11','12','13']],columns=['a','b','c','d'],index=['3'])
df_list=df_list.append(df_list2)
print(df_list)           