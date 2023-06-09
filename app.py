from flask import Flask, jsonify, request
from utilities import predict_pipeline
from google.cloud import storage
from werkzeug.utils import secure_filename
import json
import uuid
import os

app = Flask(__name__)

storage_client = storage.Client.from_service_account_json('project-capstone.json')
bucket_name = 'upload_outfithub'

@app.route('/', methods=["GET"])
def root():
     if request.method == "POST":
          return jsonify({'message': 'Connection successful', 'status': 'Success'}), 200
     else:
          return jsonify({'error': 'Only GET method is allowed', 'status': 'Failed'}), 405

@app.route("/api/v1/predict", methods=["GET", "POST"])
def predict():
     data = request.get_json()
     prediction = predict_pipeline(data)
     # prediction_json = json.dumps(prediction, indent=4)
     # return jsonify(prediction_json)
     return jsonify(prediction), 200

@app.route("/api/v1/upload", methods=["GET", "POST"])
def upload():
     try:
          storage_client.get_bucket(bucket_name)
          # return jsonify({'message': 'Connection successful', 'status': 'Success'}), 200

          if 'image' not in request.files:
               return jsonify({'error': 'No image file', 'status': 'Failed'}), 400

          image = request.files['image']
          if image.filename == '':
               return jsonify({'error': 'No image selected', 'status': 'Failed'}), 400

          #1
          # filename = secure_filename(image.filename)
          # filename = str(uuid.uuid4()) + '.' + image.filename.rsplit('.', 1)[1]

          #2
          # device_uuid = request.headers.get('X-Device-UUID')  # Mendapatkan UUID perangkat dari header request
          # filename = device_uuid + '_' + secure_filename(image.filename)
          # filename, file_extension = os.path.splitext(filename)
          # filename += file_extension

          # Menghapus file sebelumnya dengan UUID yang sama jika ada
          # existing_blob = storage_client.bucket(bucket_name).blob(filename)
          # if existing_blob.exists():
          #      existing_blob.delete()

          #3
          # filename = str(uuid.uuid4()) + '_' + secure_filename(image.filename)
          # filename, file_extension = os.path.splitext(filename)
          # filename += file_extension

          blob = storage_client.bucket(bucket_name).blob(filename)
          blob.upload_from_file(image)

          image_url = blob.public_url

          return jsonify({"image_url": image_url}), 200

     except Exception as e:
          return jsonify({'error': 'Connection failed: ' + str(e), 'status': 'Failed'}), 500

if __name__ == "__main__":
     app.run(debug=True)