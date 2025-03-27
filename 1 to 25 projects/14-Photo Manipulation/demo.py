from transform import *
from image import Image
import os

def run_demo():
    """
    Run a comprehensive demo of all image processing features
    """
    # Create output directory
    create_output_dir()
    
    # Load images
    try:
        lake = Image(filename='lake.png')
        city = Image(filename='city.png')
        print("Images loaded successfully!")
    except Exception as e:
        print(f"Error loading images: {e}")
        print("Make sure 'lake.png' and 'city.png' are in the 'input' directory.")
        return
    
    # Create a demo directory
    demo_dir = os.path.join('output', 'demo')
    if not os.path.exists(demo_dir):
        os.makedirs(demo_dir)
    
    # 1. Basic Operations
    print("\n=== Basic Operations ===")
    
    # Brightness variations
    for factor in [0.5, 1.0, 1.5, 2.0]:
        result = brighten(lake, factor)
        result.write_image(f'demo/brightness_{factor}.png')
    print("✓ Brightness variations")
    
    # Contrast variations
    for factor in [0.5, 1.0, 2.0, 3.0]:
        result = adjust_contrast(lake, factor)
        result.write_image(f'demo/contrast_{factor}.png')
    print("✓ Contrast variations")
    
    # 2. Blur Effects
    print("\n=== Blur Effects ===")
    
    # Box blur
    for size in [3, 7, 15]:
        result = blur(city, size)
        result.write_image(f'demo/box_blur_{size}.png')
    print("✓ Box blur variations")
    
    # Gaussian blur
    for sigma in [1.0, 2.0, 4.0]:
        result = gaussian_blur(city, sigma)
        result.write_image(f'demo/gaussian_{sigma}.png')
    print("✓ Gaussian blur variations")
    
    # 3. Edge Detection
    print("\n=== Edge Detection ===")
    
    # Sobel operators
    sobel_x = apply_kernel(city, np.array([
        [1, 0, -1],
        [2, 0, -2],
        [1, 0, -1]
    ]))
    sobel_x.write_image('demo/edge_x.png')
    
    sobel_y = apply_kernel(city, np.array([
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]
    ]))
    sobel_y.write_image('demo/edge_y.png')
    
    # Combined edges
    sobel_xy = combine_images(sobel_x, sobel_y)
    sobel_xy.write_image('demo/edge_combined.png')
    print("✓ Edge detection")
    
    # 4. Color Transformations
    print("\n=== Color Transformations ===")
    
    # Grayscale
    gray = grayscale(lake)
    gray.write_image('demo/grayscale.png')
    print("✓ Grayscale")
    
    # Sepia tone variations
    for intensity in [0.3, 0.6, 1.0]:
        result = sepia(lake, intensity)
        result.write_image(f'demo/sepia_{intensity}.png')
    print("✓ Sepia tone variations")
    
    # 5. Image Enhancements
    print("\n=== Image Enhancements ===")
    
    # Sharpening
    for amount in [0.5, 1.0, 2.0]:
        result = sharpen(lake, amount)
        result.write_image(f'demo/sharpen_{amount}.png')
    print("✓ Sharpening variations")
    
    # Histogram equalization
    equalized = histogram_equalization(lake)
    equalized.write_image('demo/equalized.png')
    print("✓ Histogram equalization")
    
    # 6. Special Effects
    print("\n=== Special Effects ===")
    
    # Vignette
    for strength in [0.3, 0.6, 0.9]:
        result = vignette(lake, strength)
        result.write_image(f'demo/vignette_{strength}.png')
    print("✓ Vignette effect variations")
    
    # Rotation
    for angle in [45, 90, 180]:
        result = rotate(city, angle)
        result.write_image(f'demo/rotate_{angle}.png')
    print("✓ Rotation variations")
    
    # Flipping
    flip_h = flip(city, 'horizontal')
    flip_h.write_image('demo/flip_horizontal.png')
    
    flip_v = flip(city, 'vertical')
    flip_v.write_image('demo/flip_vertical.png')
    print("✓ Flipping")
    
    # 7. Combined Effects
    print("\n=== Combined Effects ===")
    
    # Vintage photo effect
    vintage = lake
    vintage = adjust_contrast(vintage, 0.8)
    vintage = sepia(vintage, 0.7)
    vintage = vignette(vintage, 0.5)
    vintage.write_image('demo/vintage.png')
    print("✓ Vintage photo effect")
    
    # Sketch effect
    sketch = city
    sketch = grayscale(sketch)
    sketch = gaussian_blur(sketch, 1.0)
    edges = apply_kernel(sketch, np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ]))
    # Invert the edges
    sketch = Image(x_pixels=edges.x_pixels, y_pixels=edges.y_pixels, num_channels=edges.num_channels)
    sketch.array = 1.0 - edges.array
    sketch.write_image('demo/sketch.png')
    print("✓ Sketch effect")
    
    # HDR-like effect
    hdr = lake
    hdr = adjust_contrast(hdr, 1.5)
    hdr = sharpen(hdr, 1.2)
    hdr = brighten(hdr, 1.1)
    hdr.write_image('demo/hdr.png')
    print("✓ HDR-like effect")
    
    print("\nDemo completed! All images saved to the 'output/demo' directory.")

if __name__ == "__main__":
    run_demo()

