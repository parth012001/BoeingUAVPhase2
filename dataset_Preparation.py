import json
import tensorflow as tf

def load_and_preprocess_image(path, target_size=(224, 224)):
    image = tf.io.read_file(path)
    image = tf.image.decode_jpeg(image, channels=3)
    image = tf.image.resize(image, target_size)
    image /= 255.0  # Normalize to [0,1] range
    return image

def load_dataset(dataset_path, target_size=(224, 224)):
    with open(dataset_path + '/annotations.json') as f:
        annotations = json.load(f)

    def generator():
        for annotation in annotations:
            try:
                image_path = dataset_path + '/images/' + annotation['file_name']
                image = load_and_preprocess_image(image_path, target_size)

                objects = annotation['objects']
                bboxes = [obj['bbox'] for obj in objects]
                class_ids = [obj['class_id'] for obj in objects]

                yield image, {'bboxes': bboxes, 'class_ids': class_ids}
            except Exception as e:
                print(f"Error processing {annotation['file_name']}: {e}")

    return tf.data.Dataset.from_generator(
        generator,
        output_types=(tf.float32, {'bboxes': tf.float32, 'class_ids': tf.int32})
    )

# Usage
dataset = load_dataset('path/to/dataset')
