import json
import cv2

def load_inputs(measurements_path, description_path, sketch_path):
    """Loads all input data from specified files."""
    # Load measurements
    with open(measurements_path, 'r') as f:
        measurements = json.load(f)

    # Load description
    with open(description_path, 'r') as f:
        description = f.read()

    # Load sketch image
    sketch_image = cv2.imread(sketch_path)

    print(" Inputs loaded successfully.")
    return measurements, description, sketch_image