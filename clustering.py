import sklearn
import pandas as pd 
import numpy as np 

def obtain_cluster(ptrs):
       kmeans = sklearn.KMeans(n_clusters=2, random_state=0).fit(ptrs)
       return kmeans.cluster_centers_

df = pd.read_csv("convert_height_width_depth.csv")


# df.drop(df.columns.difference(['Height','Width']), 1, inplace=True)
# arr = df.to_numpy()

H = df['Height'].to_numpy()
W = df['Width'].to_numpy()
T = df['Creation Date'].to_numpy()

ptrs = np.array([[h,w] for h,w in zip(H, W)])

init = 1850
interv = 25
prev = 0
prevl = 0
clusters = []
for i, (t, ptr) in enumerate(zip(T,ptrs)):
       cur = (t - init)//interv
       if cur != prev:
              clusters.append(obtain_cluster(ptrs[prevl : i]))
              prev = cur
              prevl = i
       
print(clusters)

