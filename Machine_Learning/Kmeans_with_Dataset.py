
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
#from sklearn.linear_model import LinearRegression

Mall_custos_df = pd.read_csv('Mall_Customers.csv', names=['Customer', 'Genre', 'Age', 'Income', 'Spending'], header=0)
Mall_custos_df['Genre'] = Mall_custos_df['Genre'].replace({'Male': 0, 'Female': 1})

print(Mall_custos_df)

K = 4

kmeans = KMeans(n_clusters=K).fit(Mall_custos_df[['Age', 'Spending']])
centroidsK = kmeans.cluster_centers_
labelsK = kmeans.labels_


plt.scatter(Mall_custos_df['Age'],Mall_custos_df['Spending'], c=kmeans.labels_)
plt.scatter(centroidsK[:, 0], centroidsK[:, 1], c='red', label='Centroids')
plt.title(f"K=4")
plt.xlabel('Age')
plt.ylabel('Spending')
plt.legend(loc='upper right')
plt.show()


