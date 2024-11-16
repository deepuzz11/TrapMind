import tensorflow as tf
from models import create_model
import numpy as np

# Simulate loading attack data for training
def load_training_data():
    # Example data (features and labels)
    X_train = np.random.rand(100, 10)  # Random features
    y_train = np.random.randint(0, 2, 100)  # Random labels (0 or 1)
    return X_train, y_train

def train_model():
    model = create_model()
    X_train, y_train = load_training_data()
    model.fit(X_train, y_train, epochs=10)
    model.save('attack_behavior_model.h5')
    print("Model trained and saved.")

if __name__ == '__main__':
    train_model()
