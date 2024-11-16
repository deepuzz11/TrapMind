import numpy as np
import pandas as pd

def predict_behavior(model, new_data: pd.DataFrame):
    """
    Predict attacker behavior using the trained machine learning model.
    """
    prediction = model.predict(new_data)
    predicted_behavior = 'Attack' if prediction == 1 else 'Benign'
    print(f"Predicted Behavior: {predicted_behavior}")
    return predicted_behavior
