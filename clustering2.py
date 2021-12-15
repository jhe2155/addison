import matplotlib.pyplot as plt
import seaborn as sns 
import sklearn.cluster
import pandas as pd 
import numpy as np 
from sklearn.cluster import KMeans


# df = pd.read_csv("convert_height_width_depth.csv")

url = "https://raw.githubusercontent.com/jhe2155/addison/main/convert_height_width_depth.csv"
df = pd.read_csv(url)

def obtain_cluster(ptrs):
       kmeans = sklearn.cluster.KMeans(n_clusters=5, random_state=0).fit(ptrs)
       return kmeans.cluster_centers_

# def obtain_coordinates(ptrs):
#        kmeans = sklearn.cluster.KMeans(n_clusters=5, random_state=0).fit(ptrs)
#        return kmeans.labels_


H = df['Height'].to_numpy()
W = df['Width'].to_numpy()
T = df['Creation Date'].to_numpy()

ptrs = np.array([[h,w] for h,w in zip(H, W)])

init = 1850
interv = 25
prev = 0
prevl = 0
clusters = []
coordinates = [] 
for i, (t, ptr) in enumerate(zip(T,ptrs)):
       if t < init : continue
       cur = (t - init)//interv
       if cur != prev:
              clusters.append(obtain_cluster(ptrs[prevl : i]))
              # coordinates.append(obtain_coordinates(ptrs[prevl : i]))
              prev = cur
              prevl = i
       
print(clusters)
print(coordinates)



nlist=[]
temp = 1850
for year in clusters: 
  for c in year:
    nlist.append(c.tolist()+[temp])
  temp += 25
  # print(c)


print(nlist)

# plotn = np.concatenate(clusters, axis=0 )
# print(plotn)
plot = pd.DataFrame(nlist, columns =['x', 'y', 'year']) 
print(plot )

g= sns.scatterplot(data=plot, x="x", y="y", hue="year")

#