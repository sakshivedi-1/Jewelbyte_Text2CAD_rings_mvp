import cadquery as cq

def export_model(model, output_name):
    """
    Exports a CadQuery model to STL and STEP formats.
    
    Args:
        model (cadquery.Workplane): The CadQuery 3D model object to export.
        output_name (str): The base name for the output file (without extension).
    """
    # Define file paths
    stl_path = f"{output_name}.stl"
    step_path = f"{output_name}.step"

    # Export to STL format
    cq.exporters.export(model, stl_path)
    print(f" Model exported to {stl_path}")
    
    # Export to STEP format
    cq.exporters.export(model, step_path)
    print(f"Model exported to {step_path}")