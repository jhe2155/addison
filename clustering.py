import sklearn.cluster
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

def obtain_cluster(ptrs):
       kmeans = sklearn.cluster.KMeans(n_clusters=6, random_state=0).fit(ptrs)
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
       if t < init : continue
       cur = (t - init)//interv
       if cur != prev:
              clusters.append(obtain_cluster(ptrs[prevl : i]))
              prev = cur
              prevl = i
       
print(clusters)



fig = plt.figure()
ax = fig.add_subplot()
#ax = fig.add_subplot(projection='3d')

ax.scatter(-330,-330)
ax.scatter(330,330)

for dim in clusters[0]:
       h = dim[0]
       w = dim[1]
       print(w,h)
       rect = plt.Rectangle((-w/2, -h/2), w, h, linewidth=0.001, edgecolor='r', facecolor='none')
       ax.add_patch(rect)

rect = plt.Rectangle((-320, -180), 640, 360, linewidth=0.001, edgecolor='r', facecolor='none')
ax.add_patch(rect)

# for t, dims in enumerate(clusters):
#        for dim in dims:
#               h = dim[0]
#               w = dim[1]
#               #rect = patches.Rectangle((-w/2, -h/2), w, h, linewidth=1, edgecolor='r', facecolor='none')
#               #ax.add_patch(rect)
#               ax.scatter(dim[1], dim[0], t, c=[[0,0,t/len(clusters)]])

plt.axis('off')
#ax.set_zlabel('Z Label')
fig.savefig("cluster1.pdf", transparent=True, bbox_inches=0)
plt.show()
