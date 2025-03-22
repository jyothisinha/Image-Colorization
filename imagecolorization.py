import cv2
import numpy as np
import matplotlib.pyplot as plt
from google.colab import files

def colorize_image(input_image_path, color_map=cv2.COLORMAP_RAINBOW):
    gray_image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
    if gray_image is None:
        raise FileNotFoundError("Image file not found. Please check the path.")
    normalized_image = cv2.normalize(gray_image, None, 0, 255, cv2.NORM_MINMAX)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_image = clahe.apply(normalized_image)
    colorized_image = cv2.applyColorMap(enhanced_image, color_map)
    return colorized_image
uploaded = files.upload()
input_image_path = list(uploaded.keys())[0]
output_image_path = "colorized_image.jpg"
try:
    colorized_image = colorize_image(input_image_path, color_map=cv2.COLORMAP_TURBO)
    cv2.imwrite(output_image_path, colorized_image)

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Grayscale Image")
    plt.imshow(cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE), cmap="gray")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.title("Colorized Image")
    plt.imshow(cv2.cvtColor(colorized_image, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()

    files.download(output_image_path)

    print(f"Colorized image saved and ready for download at: {output_image_path}")
except Exception as e:
    print(str(e))