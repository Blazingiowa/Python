import pandas as pd
import numpy
import matplotlib.pyplot as plt

##LEVEL1～3##
df_list = pd.DataFrame([['1','2','3'],['4','5','6'],['7','8','9']],columns=['a','b','c'])
df_list['d']=(['x','y','z'])

df_list2 = pd.DataFrame([['10','11', '12','13']],columns=['a','b','c','d'])
df_list=df_list.append(df_list2)
df_list.index=[0,1,2,3]
print(df_list)

##LEVEL4##
df_testdata = pd.read_csv("Testdata.csv")
print(df_testdata)

##LEVEL5##
print(df_testdata.head())
print(df_testdata.tail())

##LEVEL6##
print("国語の平均："+ str(df_testdata.mean()['国語']))
print("数学の平均："+ str(df_testdata.mean()['数学']))
print("英語の平均："+ str(df_testdata.mean()['英語']))
##LEVEL7##
df_testdata['合計']=0 ##列名（カラム）は’合計’でまずは全行に値の0を代入

df_testdata['合計']=df_testdata[["国語","数学","英語"]].sum(axis=1)
print(df_testdata)

##LEVEL8##
##’順位’の列を追加して、合計の降順にランク（1～10）を付ける
df_testdata['順位']=df_testdata[['合計']].rank(ascending=False)
print(df_testdata)
#順位の昇順（合計の降順）にDataFrameを整列
df_testdata=df_testdata.sort_values('順位')
print(df_testdata)

##LEVEL9##
plt.xticks(df_testdata['ID'], rotation=0)#表示が省略されないようにする
plt.bar(df_testdata['ID'],df_testdata['合計'])
plt.show()

##LEVEL10##
colorlist = ["r", "g", "b", "c", "m", "y", "k", "#ff2255", "#ffaa00", "#00aaff"]
plt.bar(df_testdata['ID'],df_testdata['合計'],color=colorlist)
plt.savefig('plot.png', bbox_inches='tight')##bbox_inches='tight'は余白を小さくする