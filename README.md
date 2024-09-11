# Image-Noise-Generator-Application

# Image Noise App

## Overview

The **Image Noise App** is a Python application built using the Tkinter library for graphical user interfaces. It allows users to load images, apply various noise and distortion effects, and save the modified images. The app provides several image manipulation features including blur, glitch effects, Gaussian noise, and salt-and-pepper noise.

## Features

- **Load Images**: Load one or more images from your file system.
- **Add Blur**: Apply a Gaussian blur effect to the images.
- **Add Glitch**: Apply a glitch effect to create visual distortions.
- **Add Enhanced Glitch**: Apply an advanced glitch effect with color channel shifts.
- **Add Gaussian Noise**: Introduce Gaussian noise to the images.
- **Add Salt and Pepper Noise**: Apply salt and pepper noise to the images.
- **Save Images**: Save the noisy images to your chosen directory.

## Requirements

- Python 3.x
- `tkinter` (standard library, no installation required)
- `Pillow` (PIL fork) - for image processing: `pip install pillow`
- `numpy` - for numerical operations: `pip install numpy`
- `opencv-python` - for adding Gaussian noise: `pip install opencv-python`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/imagenoiseapp.git
   ```
2. Navigate to the project directory:
   ```bash
   cd imagenoiseapp
   ```
3. Install the required Python packages:
   ```bash
   pip install pillow numpy opencv-python
   ```

## Usage

1. Run the application:
   ```bash
   python image_noise_app.py
   ```
2. Use the buttons on the left side of the window to interact with the application:
   - **Load Images**: Select images from your file system to load into the application.
   - **Add Blur**: Apply a Gaussian blur effect to the loaded images.
   - **Add Glitch**: Apply a glitch effect to the images.
   - **Add Enhanced Glitch**: Apply an advanced glitch effect with color channel shifts.
   - **Add Gaussian Noise**: Introduce Gaussian noise to the images.
   - **Add Salt and Pepper Noise**: Apply salt and pepper noise to the images.
   - **Save Images**: Save the modified images to your chosen directory.

## Code Overview

### Functions

- **`add_blur(image)`**: Applies a Gaussian blur effect to the input image.
- **`add_distortion(image)`**: Distorts the image using a perspective transformation.
- **`add_glitch(image)`**: Applies a basic glitch effect with random horizontal and vertical displacements.
- **`add_enhanced_glitch(image)`**: Applies an advanced glitch effect with color channel shifts.
- **`add_gaussian_noise(image, mean=0, std=25)`**: Adds Gaussian noise to the image.
- **`add_salt_and_pepper(image, salt_prob=0.02, pepper_prob=0.02)`**: Adds salt and pepper noise to the image.

### `ImageNoiseApp` Class

- **`__init__(self, root)`**: Initializes the Tkinter window and sets up the UI.
- **`load_images(self)`**: Opens a file dialog to load images.
- **`display_image(self, image)`**: Displays the given image in the Tkinter window.
- **`apply_noise_to_images(self, noise_function)`**: Applies the specified noise function to all loaded images.
- **`apply_blur(self)`**: Applies the blur effect to the images.
- **`apply_glitch(self)`**: Applies the glitch effect to the images.
- **`apply_enhanced_glitch(self)`**: Applies the enhanced glitch effect to the images.
- **`apply_gaussian_noise(self)`**: Applies Gaussian noise to the images.
- **`apply_salt_and_pepper(self)`**: Applies salt and pepper noise to the images.
- **`save_images(self)`**: Opens a file dialog to select a directory and saves the modified images.

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the existing style and includes appropriate documentation.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please open an issue on the GitHub repository or contact [your email].

---

Feel free to customize the contact information and add any additional details relevant to your project.
