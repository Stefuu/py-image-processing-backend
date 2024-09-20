import os
from flask import Flask, request, jsonify, send_from_directory
from lego_mosaic_A4 import process_image
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
CORS(app, resources={r"/uploads/*": {"origins": "http://127.0.0.1:5500"}})

# Absolute paths for the upload and processed images directories
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
PROCESSED_FOLDER = os.path.join(BASE_DIR, 'processed_images')

@app.route('/')
def index():
    return 'Servidor Flask está funcionando!'

@app.route('/uploads', methods=["POST", "GET"]) 
def upload_file(): 
    if 'file' not in request.files:
        return 'No file part', 400
     
    file = request.files['file']  

    if file.filename == '':    
        return 'No selected file', 400

    # Full path to save the original file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path) 

    # Name of the processed file
    output_filename = 'output_image_processed.jpg'  

    # Call the image processing function, which saves the processed image
    process_image(file_path)  # Ensure this function saves the output in PROCESSED_FOLDER

    # Return the URL of the processed image
    return jsonify({'image_url': f'/processed_images/{output_filename}'})

@app.route('/processed_images/<filename>')
def get_processed_image(filename):
    # Send the processed image file
    return send_from_directory(PROCESSED_FOLDER, filename) 

if __name__ == '__main__': 
    app.run(debug=True)
