import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageFilter, ImageOps
import numpy as np
import cv2
import os

def add_blur(image):
    return image.filter(ImageFilter.GaussianBlur(radius=5))

def add_distortion(image):
    width, height = image.size
    new_image = image.transform(
        (width, height), Image.QUAD, (0, 0, width, 0, width, height, 0, height), resample=Image.BICUBIC
    )
    return new_image

def add_glitch(image):
    image = image.convert('RGB')  # Ensure image is in RGB mode
    image_array = np.array(image)
    rows, cols, _ = image_array.shape

    # Horizontal displacement
    for i in range(rows):
        if np.random.rand() < 0.1:  # Apply glitch to 10% of the rows
            displacement = np.random.randint(5, 50)
            image_array[i] = np.roll(image_array[i], displacement, axis=0)

    # Vertical displacement
    for i in range(cols):
        if np.random.rand() < 0.1:  # Apply glitch to 10% of the columns
            displacement = np.random.randint(5, 50)
            image_array[:, i] = np.roll(image_array[:, i], displacement, axis=0)

    # Color channel manipulation
    if np.random.rand() < 0.5:
        image_array[:, :, 0] = np.roll(image_array[:, :, 0], np.random.randint(-5, 5), axis=0)
    if np.random.rand() < 0.5:
        image_array[:, :, 1] = np.roll(image_array[:, :, 1], np.random.randint(-5, 5), axis=0)
    if np.random.rand() < 0.5:
        image_array[:, :, 2] = np.roll(image_array[:, :, 2], np.random.randint(-5, 5), axis=0)

    return Image.fromarray(image_array)

def add_enhanced_glitch(image):
    image = image.convert('RGB')  # Ensure image is in RGB mode
    image_array = np.array(image)
    rows, cols, _ = image_array.shape

    # Create color channel shifts
    def shift_channel(image_array, channel, max_shift):
        shift = np.random.randint(-max_shift, max_shift)
        shifted = np.roll(image_array[:, :, channel], shift, axis=1)
        if shift > 0:
            shifted[:, :shift] = 0
        elif shift < 0:
            shifted[:, shift:] = 0
        image_array[:, :, channel] = shifted
        return image_array

    # Apply channel shifts
    for channel in range(3):
        image_array = shift_channel(image_array, channel, max_shift=50)

    return Image.fromarray(image_array)

def add_gaussian_noise(image, mean=0, std=25):
    image = image.convert('RGB')  # Ensure image is in RGB mode
    image_array = np.array(image)
    noise = np.random.normal(mean, std, image_array.shape).astype(np.uint8)
    noisy_image = cv2.add(image_array, noise)
    return Image.fromarray(noisy_image)

def add_salt_and_pepper(image, salt_prob=0.02, pepper_prob=0.02):
    image = image.convert('RGB')  # Ensure image is in RGB mode
    image_array = np.array(image)
    rows, cols, _ = image_array.shape
    
    # Add salt noise
    num_salt = np.ceil(salt_prob * image_array.size)
    coords = [np.random.randint(0, i, int(num_salt)) for i in image_array.shape]
    image_array[coords[0], coords[1], :] = 255
    
    # Add pepper noise
    num_pepper = np.ceil(pepper_prob * image_array.size)
    coords = [np.random.randint(0, i, int(num_pepper)) for i in image_array.shape]
    image_array[coords[0], coords[1], :] = 0
    
    return Image.fromarray(image_array)

class ImageNoiseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Noise App")
        self.root.geometry("1000x600")
        self.root.config(bg='#2e2e2e')
        
        self.frame = tk.Frame(self.root, bg='#2e2e2e')
        self.frame.pack(side=tk.LEFT, fill=tk.Y)

        self.panel = tk.Label(self.root, bg='#2e2e2e')
        self.panel.pack(side=tk.RIGHT, expand=True)

        button_width = 20
        button_style = {
            'bg': '#3c3c3c', 
            'fg': 'white', 
            'activebackground': '#5a5a5a',
            'activeforeground': 'white',
            'font': ('Arial', 12, 'bold'),
            'bd': 0,
            'highlightthickness': 0,
            'width': button_width
        }

        buttons = [
            ("Load Images", self.load_images),
            ("Add Blur", self.apply_blur),
            ("Add Glitch", self.apply_glitch),
            ("Add Enhanced Glitch", self.apply_enhanced_glitch),
            ("Add Gaussian Noise", self.apply_gaussian_noise),
            ("Add Salt and Pepper Noise", self.apply_salt_and_pepper),
            ("Save Images", self.save_images)
        ]

        for text, command in buttons:
            button = tk.Button(self.frame, text=text, command=command, **button_style)
            button.pack(pady=10)

        self.images = []
        self.noisy_images = []

    def load_images(self):
        file_paths = filedialog.askopenfilenames()
        if file_paths:
            self.images = [Image.open(file_path).convert('RGB') for file_path in file_paths]  # Convert to RGB
            self.noisy_images = []
            self.display_image(self.images[0])

    def display_image(self, image):
        image = image.resize((600, 600))
        self.imgtk = ImageTk.PhotoImage(image)
        self.panel.config(image=self.imgtk)
        self.panel.image = self.imgtk

    def apply_noise_to_images(self, noise_function):
        if self.images:
            self.noisy_images = [noise_function(image) for image in self.images]
            self.display_image(self.noisy_images[0])

    def apply_blur(self):
        self.apply_noise_to_images(add_blur)

    def apply_glitch(self):
        self.apply_noise_to_images(add_glitch)

    def apply_enhanced_glitch(self):
        self.apply_noise_to_images(add_enhanced_glitch)

    def apply_gaussian_noise(self):
        self.apply_noise_to_images(add_gaussian_noise)

    def apply_salt_and_pepper(self):
        self.apply_noise_to_images(add_salt_and_pepper)

    def save_images(self):
        if self.noisy_images:
            dir_path = filedialog.askdirectory()
            if dir_path:
                for i, noisy_image in enumerate(self.noisy_images):
                    file_path = os.path.join(dir_path, f"noisy_image_{i}.png")
                    noisy_image.save(file_path)
                messagebox.showinfo("Save Images", "Images saved successfully.")

def open_manual_images_window():
    root = tk.Tk()
    app = ImageNoiseApp(root)
    root.mainloop()

open_manual_images_window()
