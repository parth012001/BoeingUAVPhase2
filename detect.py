import cv2
import tensorflow as tf
from model import create_model

def preprocess_image_opencv(image, target_size=(224, 224)):
    # Resize and normalize the image
    image = cv2.resize(image, target_size)
    image = image / 255.0
    return image

def detect_objects(image_path, model, target_size=(224, 224)):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image {image_path}")
        return

    # Preprocess the image
    preprocessed_image = preprocess_image_opencv(image, target_size)
    preprocessed_image = np.expand_dims(preprocessed_image, axis=0)  # Add batch dimension

    # Make predictions
    predictions = model.predict(preprocessed_image)

    # Process and display the results
    # This part depends on how your model outputs predictions
    # For example, if it outputs bounding boxes and class IDs:
    # for bbox, class_id in zip(predictions['bboxes'], predictions['class_ids']):
    #     # Draw bounding box and label on the image
    #     # Convert bbox coordinates to integer
    #     # Use cv2.rectangle and cv2.putText to draw on the image

    # Display the image with predictions
    cv2.imshow("Predictions", image)
    cv2.waitKey(0)  # Wait for a key press to close the displayed image
    cv2.destroyAllWindows()

# Load the model
model = create_model()
model.load_weights('path/to/model/weights')

# Test the function
detect_objects('path/to/test/image.jpg', model)
