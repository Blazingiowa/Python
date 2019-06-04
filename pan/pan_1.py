import pandas as pd

df_list = pd.DataFrame([['1','2','3'],['4','5','6'],['7','8','9']],columns=['a','b','c'])
df_list['d']=(['x','y','z'])
print(df_list)