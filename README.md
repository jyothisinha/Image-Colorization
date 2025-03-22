# Image-Colorization
This Python script enhances and colorizes grayscale images using OpenCV's color maps. It applies CLAHE (Contrast Limited Adaptive Histogram Equalization) for better contrast before colorizing the image.

Features

1. Converts a grayscale image into a colorized version using OpenCV color maps

2. Uses CLAHE to enhance contrast before applying color mapping

3. Supports multiple color maps (default: COLORMAP_TURBO)

4. Displays the original and colorized images side by side using Matplotlib

5. Saves and allows downloading of the colorized image

Requirements

1. OpenCV (cv2)

2. NumPy (numpy)

3. Matplotlib (matplotlib)

4. Google Colab (files module for uploading and downloading images)

Usage

1. Upload a grayscale image using Google Colab's files.upload().

2. The script processes the image, enhances it using CLAHE, and applies the selected color map.

3. The original and colorized images are displayed side by side.

4. The colorized image is saved as colorized_image.jpg and made available for download.
