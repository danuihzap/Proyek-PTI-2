import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("apbn.csv")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 100)
pd.set_option('expand_frame_repr', True)
print(df)

#dimensi csv
print(df.shape[0]," ",df.shape[1])
print(df.groupby(["tahun","pos_belanja"])["nilai"].sum())
#grafik total APBN per tahun

dfsum=df.groupby(["tahun"])["nilai"].sum()
print(dfsum)
'''
dfsum.plot(kind = "line",title="Total APBN per Tahun",x="tahun",y="jumlah")
plt.xlabel("Tahun")
plt.ylabel("Jumlah Pengeluaran")
plt.show()
plt.clf()
#
df.groupby(["tahun","tipe_pengeluaran"])["nilai"].sum().unstack().plot(kind="bar",title="Pengeluaran Berdasarkan Tipe Pengeluaran", stacked = True)
plt.xlabel("Tahun")
plt.ylabel("Jumlah Pengeluaran")
plt.show()
plt.clf()

df.groupby(["tahun","pos_belanja"])["nilai"].sum().unstack().plot(kind="line",title="Pengeluaran Berdasarkan Pos Belanja")
plt.xlabel("Tahun")
plt.ylabel("Jumlah Pengeluaran")
plt.show()
plt.clf()

df.loc[df["tipe_pengeluaran"] == "'Dana Perimbangan'"].groupby(["tahun","tipe_pengeluaran"]).sum().unstack().plot(kind = "bar",title="Total Dana Perimbangan")
plt.xlabel("Tahun")
plt.ylabel("Jumlah Pengeluaran")
plt.show()
plt.clf()

df.groupby(["tahun","keterangan_pengeluaran"])["nilai"].sum().unstack().plot(kind="line",title="Korelasi Tiap Pengeluaran")
plt.xlabel("Tahun")
plt.ylabel("Jumlah Pengeluaran")
plt.show()
plt.clf()
'''
dfsum2 = pd.DataFrame(dfsum)
print(df["nilai"].describe())
print(df["nilai"].quantile([.1,.2,.3,.4,.5,.6,.7,.8,.9,1]))
print(dfsum.describe())
print(dfsum.quantile([.1,.2,.3,.4,.5,.6,.7,.8,.9,1]))
print(dfsum2[:,0].corr(dfsum2[:,1]))

#plt.show()
