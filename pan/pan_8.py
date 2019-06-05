import pandas as pd
df=pd.read_csv('Testdata.csv')
col_list=list(df)
col_list.remove('ID')
df['合計']=df[col_list].sum(axis=1)
df['順位']=[0]*10
print(df)