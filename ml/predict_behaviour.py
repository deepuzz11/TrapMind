import tensorflow as tf
import numpy as np

# Load trained model and predict attack behavior
def predict_behavior(input_data):
    model = tf.keras.models.load_model('attack_behavior_model.h5')
    prediction = model.predict(np.array([input_data]))
    return prediction

# Example usage
if __name__ == '__main__':
    example_input = np.random.rand(10)  # Random input data
    prediction = predict_behavior(example_input)
    print(f"Predicted behavior: {prediction}")
