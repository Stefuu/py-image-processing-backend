import cv2
import os

def process_image(file_path):
    # Read the image
    image = cv2.imread(file_path)

    # Perform image processing (e.g., convert to grayscale)
    processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Define the output path
    output_path = os.path.join(os.path.dirname(__file__), 'processed_images', 'output_image_processed.jpg')

    # Save the processed image
    cv2.imwrite(output_path, processed_image)
