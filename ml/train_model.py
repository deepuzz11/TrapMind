import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model(data: pd.DataFrame):
    """
    Train a machine learning model to detect attack patterns based on input data.
    """
    # Assuming 'label' column contains attack type (e.g., 1 for attack, 0 for benign)
    X = data.drop('label', axis=1)  # Features (e.g., network traffic, commands)
    y = data['label']  # Labels (attack type)

    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train a RandomForest model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Evaluate the model
    accuracy = model.score(X_test, y_test)
    print(f"Model Accuracy: {accuracy}")
    
    return model
