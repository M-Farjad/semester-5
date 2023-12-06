# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris_data = pd.read_csv(url, names=names)

# Separate features and target variable
X = iris_data.iloc[:, :-1].values
y = iris_data.iloc[:, -1].values

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
y_kmeans = kmeans.fit_predict(X_scaled)

# Visualize the clusters
plt.scatter(X_scaled[y_kmeans == 0, 0], X_scaled[y_kmeans == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X_scaled[y_kmeans == 1, 0], X_scaled[y_kmeans == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(X_scaled[y_kmeans == 2, 0], X_scaled[y_kmeans == 2, 1], s=100, c='green', label='Cluster 3')

plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
plt.title('K-means Clustering of Iris Dataset')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend()
plt.show()

# Save the K-means model
joblib.dump(kmeans, 'kmeans_model.joblib')

# Load the model for testing
loaded_kmeans = joblib.load('kmeans_model.joblib')

# Take input from the user for prediction
user_input = []
user_input.append(float(input("Enter Sepal length in cm: ")))
user_input.append(float(input("Enter Sepal width in cm: ")))
user_input.append(float(input("Enter Petal length in cm: ")))
user_input.append(float(input("Enter Petal width in cm: ")))

# Scale the user input
scaled_user_input = scaler.transform([user_input])

# Get the prediction
user_prediction = loaded_kmeans.predict(scaled_user_input)
predicted_class = np.unique(y)[user_prediction[0]]

# Display the predicted class
print(f"\nPredicted attribute: class of iris plant - {predicted_class}")
