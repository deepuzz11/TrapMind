import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Example ML Model
def train_model(data):
    model = RandomForestClassifier()
    X = data.drop('label', axis=1)  # Features
    y = data['label']  # Labels
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f"Model Accuracy: {accuracy}")
    return model
