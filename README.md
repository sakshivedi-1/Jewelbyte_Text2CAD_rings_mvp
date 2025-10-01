# Jewelbyte_Text2CAD_rings_mvp
This project is a functional prototype of a pipeline that converts a set of inputs—key measurements, a natural language description, and a 2D sketch—into a precise, manufacturable 3D CAD model of a solitaire ring. The pipeline is built with a focus on modularity, accuracy, and scalability.

The final output consists of industry-standard .stl (for 3D printing) and .step (for high-fidelity CAD work) files that are dimensionally accurate and production-ready.

# Key Features
Parametric Generation: Automatically creates a 3D model based on precise measurements from a .json file.

Modular Architecture: The code is cleanly separated into data ingestion, geometry generation, and file export stages, making it easy to maintain and extend.

Production-Ready Output: Generates watertight solid models in both STL and STEP formats, ensuring compatibility with manufacturing and other CAD software like Rhino.

Proof-of-Concept Sketch Analysis: Includes a function for basic image processing of sketches using OpenCV.


# Architecture
The pipeline is designed with a simple, three-stage modular architecture. This separation of concerns allows for easy modification and scaling of any individual component without affecting the others.

Jewelbytes_text2CAD_rings/
│
├── main.py # Orchestrator script that runs the pipeline
│
├── data_ingestion/ # Module: Handles input data
│ └── parser.py # Reads and parses all input files
│
├── geometry_generation/ # Module: Core CAD generation
│ └── ring_generator.py # Builds the 3D model using CadQuery
│
├── file_export/ # Module: Export utilities
│ └── exporter.py # Saves the final model to .stl and .step
│
├── inputs/ # Input files directory
│ ├── measurements.json # Key parameters (ring size, band width, stone dia)
│ ├── description.txt # Natural language description (metadata)
│ └── sketch.png # 2D sketch (hand-drawn / AI generated)
│
└── outputs/ # Output directory for final CAD files
  #(Generated .3dm / .stl / .step files)

Data Ingestion: The parser.py module reads the measurements.json, description.txt, and sketch.png files from the /inputs directory.

Geometry Generation: The ring_generator.py module takes the parsed measurements and uses the CadQuery library to parametrically construct the 3D geometry of the ring, stone, and prongs.

File Export: The exporter.py module receives the final 3D object from the generator and saves it in the /outputs directory.

# Technology Stack
Python 3: The core programming language.

CadQuery: The primary library for parametric 3D CAD modeling.

OpenCV: Used for basic image processing of the 2D sketch.

NumPy: A dependency for OpenCV.

Installation & Setup
This project uses a virtual environment to ensure dependencies are handled cleanly.

Clone the repository:

Bash

git clone <your-repo-url>
cd text-to-cad-ring
Create a virtual environment:

Bash

python -m venv venv
Activate the virtual environment:

On Windows:

Bash

.\venv\Scripts\Activate
On macOS/Linux:

Bash

source venv/bin/activate
Your terminal prompt should now start with (venv).

Install the required packages:

Bash

pip install cadquery opencv-python numpy
(Alternatively, create a requirements.txt file and use pip install -r requirements.txt)

Testing Instructions & Usage
To test the pipeline and generate a new model, follow these steps:

Modify the Inputs:

Open the inputs/measurements.json file.

Change the values for ring_size_us, band_width_mm, stone_diameter_mm, etc., to define a new ring.

Run the Pipeline:

Make sure your virtual environment is active ((venv) is in your terminal prompt).

Execute the main script from the root directory:

Bash

python main.py
Check the Output:

The terminal will print success messages.

Navigate to the outputs/ folder.

You will find generated_ring.stl and generated_ring.step. You can open the .step file in any CAD software (Rhino, FreeCAD, Fusion 360) to inspect and measure the model.

Design Decisions
Several key decisions were made during the development of this pipeline:

Initial Choice of rhino3dm: The project was initially started with the rhino3dm library to leverage its native compatibility with Rhino software.

Strategic Pivot to CadQuery: During development, persistent environment and library versioning issues with rhino3dm proved to be a significant obstacle, leading to a chain of AttributeError exceptions. A strategic decision was made to pivot to CadQuery. This was the most critical decision in the project, as it resolved all environment issues and resulted in a more stable, robust, and maintainable pipeline. CadQuery's modern, Python-native API also proved to be highly intuitive and efficient for parametric modeling.

Choice of Output Formats:

STEP (.step): Chosen over Rhino's proprietary .3dm format because it is a universal, high-fidelity standard for sharing precise geometry between all major CAD programs.

STL (.stl): Included as it is the universal standard for 3D printing and mesh-based applications.

# Limitations & Future Work
This prototype successfully lays the foundation for a more advanced system but has several limitations:

Limited Geometry: The current version only generates a classic four-prong solitaire ring with a round stone.

Basic Sketch Integration: The sketch analysis function exists but is not fully integrated to drive the geometry and works best with very clean, simple profile images.

Text as Metadata: The natural language description is stored as metadata but is not yet used to influence the design.

Future work could focus on:

Expanding the Design Library: Add more stone shapes (princess, oval), setting types (bezel, pavé), and band styles.

Advanced NLP: Integrate Natural Language Processing to parse keywords from the description (e.g., "twisted band," "six prongs") to automatically modify the generated model.

Robust Sketch-to-Profile: Improve the computer vision model to reliably extract complex profiles from hand-drawn sketches.

User Interface: Build a simple web-based UI (using Streamlit or Flask) to allow users to input parameters and upload files without editing them manually.











# A simple lookup for US ring sizes to inner diameter in mm

RING_SIZE_TO_DIAME
