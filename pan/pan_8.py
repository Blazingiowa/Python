import pandas as pd
df=pd.read_csv('Testdata.csv')
df['合計']=df[['国語','数学','英語']].sum(axis=1)
df['順位']=df['合計'].rank(ascending=False)
df=df.sort_values('順位')
print(df)