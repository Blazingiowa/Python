import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('kion10y.csv',encoding="utf-8")

atui_bool=(df["気温"]>30)
atui=df[atui_bool]
cnt=atui.groupby(["年"])["年"].count()

print(cnt)
cnt.plot()
plt.savefig("tenki-over30.png")
plt.show()