import tensorflow as tf
from dataset_preparation import load_dataset
from model import create_model

model = create_model()
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Load your dataset
train_dataset, val_dataset = load_dataset('path/to/dataset')

model.fit(train_dataset, epochs=10, validation_data=val_dataset)
