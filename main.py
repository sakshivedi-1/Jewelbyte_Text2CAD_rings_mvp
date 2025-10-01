# main.py
import os
from data_ingestion import parser
from geometry_generation import ring_generator
from file_export import exporter

def main():
    """
    Runs the full Text-to-CAD pipeline.
    """
    # --- 1. Data Ingestion ---
    # Define paths to input files
    input_dir = 'inputs'
    measurements_path = os.path.join(input_dir, 'measurements.json')
    description_path = os.path.join(input_dir, 'description.txt')
    sketch_path = os.path.join(input_dir, 'sketch.png')

    # Load data using the parser module
    try:
        measurements, description, sketch_image = parser.load_inputs(
            measurements_path, description_path, sketch_path
        )
    except FileNotFoundError as e:
        print(f"Error: Input file not found. {e}")
        return

    # --- 2. Geometry Generation ---
    print("Generating 3D model...")
    try:
        # Extract parameters from the loaded measurements
        ring_model = ring_generator.create_parametric_ring(
            ring_size_us=measurements.get("ring_size_us"),
            band_width=measurements.get("band_width_mm"),
            band_thickness=measurements.get("band_thickness_mm"),
            stone_diameter=measurements.get("stone_diameter_mm")
        )
        # Store description as metadata in the file
        ring_model.Notes = description

    except (ValueError, KeyError) as e:
        print(f"Error during geometry generation: {e}")
        return
    
    print(" Model generated successfully.")

    # --- 3. File Export ---
    # Create an output directory if it doesn't exist
    output_dir = 'outputs'
    os.makedirs(output_dir, exist_ok=True)
    output_filename = os.path.join(output_dir, "generated_ring")

    exporter.export_model(ring_model, output_filename)
    
    print("\n Pipeline finished successfully!")

if __name__ == '__main__':
    main()