#k-means and k-means++
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from pandas import DataFrame
import numpy as np

Data = {
	    'x': [35,34,32,37,33,33,31,27,35,34,62,54,57,47,50,57,59,52,61,47,50,48,39,40,45,47,39,44,50,48],
        'y': [79,54,52,77,59,74,73,57,69,75,51,32,40,47,53,36,35,58,59,50,23,22,13,14,22,7,29,25,9,8]
       }
  
#df = DataFrame(Data,columns=['x','y'])
df = DataFrame(Data)
print(df)

#kmeans = KMeans(n_clusters=3).fit(df) #k-means
kmeans = KMeans(n_clusters=3, init = 'k-means++').fit(df) #k-means++


centroidsK = kmeans.cluster_centers_ #coordinates of cluster centers (centroids)
labelsK = kmeans.labels_ #labels/clusters each data point belongs to

print(f'Centroids:\n{centroidsK}')
print()
print(f'Labels:\n{labelsK}')

data_points = np.array([[34, 52], [48, 6], [62, 49], [35, 77]])

def predict(x, centroids):
    # documentation ref: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
    # https://github.com/scikit-learn/scikit-learn/blob/6e9039160/sklearn/linear_model/_base.py#L292

    # passes numpy array
    # calc euclidean distances from points to centroids
    distances = np.linalg.norm(x[:, np.newaxis] - centroids, axis=2)
    labels = np.argmin(distances, axis=1)
    return labels


predictions = predict(data_points, centroidsK)    
print(f'Predictions:', predictions)

# comparison with .predict
sklearn_predictions = kmeans.predict(data_points)
print('Sklearn Predictions:', sklearn_predictions)

plt.scatter(df['x'], df['y'], c=labelsK) 
plt.scatter(centroidsK[:, 0], centroidsK[:, 1], c='red', label='centroids')
plt.scatter(data_points[:, 0], data_points[:, 1], c='blue', marker='+', s=150, label='predicted') 
plt.legend(loc='upper right')
plt.title('K=3')
plt.xlabel('x')
plt.ylabel('y')
plt.show()