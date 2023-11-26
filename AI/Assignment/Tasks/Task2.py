import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load the Iris dataset
data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header=None, names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

# Standardize the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']])

# Create a KMeans model with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)

# Fit the model to the data
kmeans.fit(scaled_data)

# Predict the cluster labels
labels = kmeans.predict(scaled_data)

# Visualize the clusters
plt.figure(figsize=(8, 6))
plt.scatter(data['sepal_length'], data['petal_length'], c=labels)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.title('Iris Clusters')
plt.show()
