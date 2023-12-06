import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = np.array([
    [1, 'Sunny', 'Hot', 'High', 'No'],
    [2, 'Sunny', 'Hot', 'High', 'No'],
    [3, 'Overcast', 'Hot', 'High', 'Yes'],
    [4, 'Rainy', 'Mild', 'High', 'Yes'],
    [5, 'Rainy', 'Cool', 'Normal', 'Yes'],
    [6, 'Rainy', 'Cool', 'Normal', 'No'],
    [7, 'Overcast', 'Cool', 'Normal', 'Yes'],
    [8, 'Sunny', 'Mild', 'High', 'No'],
    [9, 'Sunny', 'Cool', 'Normal', 'Yes'],
    [10, 'Rainy', 'Mild', 'Normal', 'Yes']
])

X = data[:, 1:4]
y = data[:, 4]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=0)

def calculate_probabilities(data,label_column):
    probabilities = {}
    labels, counts = np.unique(data[:, label_column], return_counts=True)
    total_samples = len(data)
    for label, count in zip(labels, counts):
        probabilities[label] = count / float(total_samples)
    return probabilities

def train_naive_bayes(X,y):
    num_features =X.shape[1]
    unique_labels = np.unique(y)
    probabilities = {}
    for label in unique_labels:
        label_indices = np.where(y == label)[0]
        label_data = X[label_indices]

        probabilities[label] = []
        for i in range(num_features):
            feature_values, count = np.unique(label_data[:,i],return_counts=True)
            feature_probabilities = dict(zip(feature_values,count/len(label_data)))
            probabilities[label].append(feature_probabilities)
    return probabilities

def predict_naive_bayes(intsance,probabilities):
    predicted_label = None
    max_probability = -1

    for label, label_probabilities in probabilities.items():
        instance_probability = 1.0
        for i, value in enumerate(intsance):
            if value in label_probabilities[i]:
                instance_probability *= label_probabilities[i][value]
            else:
                instance_probability = 0

        if instance_probability > max_probability:
            max_probability = instance_probability
            predicted_label = label
    return predicted_label

probabilities = train_naive_bayes(X,y)

test_instance = ['Sunny', 'Cool', 'High']
predicted_label = predict_naive_bayes(test_instance,probabilities)

print(f'the predicted label for the instance {test_instance} is: {predicted_label}')