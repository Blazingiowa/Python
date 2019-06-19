import urllib.request as req
import pandas as pd

url = "https://raw.githubsercontent.com/pandas-dev/master/pandas/tests/data/iris.csv"
savefile="iris.csv"
req.urlretrieve(url, savefile)
print("保存しました")

csv=pd.read_csv(savefile, encoding="utf-8")
csv