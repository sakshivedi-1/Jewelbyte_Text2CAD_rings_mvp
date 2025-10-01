import cadquery as cq
import math

# A simple lookup for US ring sizes to inner diameter in mm
RING_SIZE_TO_DIAMETER = {
    '6': 16.51,
    '7': 17.35,
    '8': 18.19,
    '9': 18.89,
}

def create_parametric_ring(ring_size_us, band_width, band_thickness, stone_diameter):
    #  Calculate dimensions
    try:
        ring_inner_diameter = RING_SIZE_TO_DIAMETER[str(ring_size_us)]
    except KeyError:
        raise ValueError(f"Ring size '{ring_size_us}' not supported. Please use one of {list(RING_SIZE_TO_DIAMETER.keys())}.")
    
    ring_inner_radius = ring_inner_diameter / 2.0
    stone_radius = stone_diameter / 2.0

    #  Create the Ring Band by revolving a rectangular profile
    # The band profile: thickness (radial) x width (vertical height)
    band = (
        cq.Workplane("XZ")  # Create a sketch on the XZ plane (side view)
        .rect(band_thickness, band_width, centered=(False, True))  # Cross-section of the band
        .translate((ring_inner_radius, 0))  # Position at inner radius
        .revolve(360, (0, 0, 0), (0, 1, 0))  # Revolve around Y-axis
    )

    #  Create the Center Stone
    # Position the stone to sit above the band
    # Stone should rest on top of the band with some clearance
    stone_center_height = band_width/2 + stone_radius * 0.7  # Stone sits partially above band
    stone = (
        cq.Workplane("XY")  # Start on the XY plane (top view)
        .sphere(stone_radius)
        .translate((0, 0, stone_center_height))
    )

    #  Create Prongs
    prong_radius = 0.5  # Slightly smaller prongs for proportion
    prong_height = stone_radius * 1.2  # Prong height relative to stone
    prong_base_height = stone_center_height - stone_radius * 0.5  # Start below stone center
    
    prongs = cq.Workplane("XY")  # Start a new empty workplane for the prongs

    # Loop and create four prongs evenly spaced around the stone
    for angle in [45, 135, 225, 315]:
        # Convert angle to radians
        angle_rad = math.radians(angle)
        
        # Calculate prong position at stone surface
        prong_x = stone_radius * 0.8 * math.cos(angle_rad)  # 0.8 to place on stone surface
        prong_y = stone_radius * 0.8 * math.sin(angle_rad)
        
        # Create a cylinder for the prong
        prong = (
            cq.Workplane("XY")
            .cylinder(prong_height, prong_radius)
            .translate((prong_x, prong_y, prong_base_height + prong_height/2))
        )
        
        prongs = prongs.union(prong)

    #  Combine all parts into a single solid model
    final_ring = band.union(stone).union(prongs)

    return final_ring