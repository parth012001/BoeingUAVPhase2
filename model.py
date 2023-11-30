import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2

def create_model():
    base_model = MobileNetV2(input_shape=(128, 128, 3), include_top=False)
    base_model.trainable = False  # Freeze the base model
    global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
    prediction_layer = tf.keras.layers.Dense(1)
    model = tf.keras.Sequential([
        base_model,
        global_average_layer,
        prediction_layer
    ])
    return model
