
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

house_df = pd.read_csv('housing.csv')

Data = {
            'x': np.array(house_df["Longitude"]),
            'y': (house_df["Latitude"])
    }

house_df = pd.DataFrame(Data)

K = 6

kmeans = KMeans(n_clusters=K).fit(house_df)

centroidsK = kmeans.cluster_centers_
labelsK = kmeans.labels_

plt.scatter(house_df['x'],house_df['y'], c=kmeans.labels_)
plt.scatter(centroidsK[:, 0], centroidsK[:, 1], c='red', label='Centroids')
plt.title(f"KMeans Clustering")
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend(loc='upper right')
plt.show()