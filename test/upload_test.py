# import requests
# from flask import jsonify
# import json

# image1 = "https://media.istockphoto.com/id/609694758/id/foto/berdiri-tegak.jpg?s=1024x1024&w=is&k=20&c=4Z7qxTaOE0zmC8UH5_gpbh-Rq3q6T6Am6aW9-o6Jx3U="
# payload = {'image': image1}

# resp = requests.post("http://127.0.0.1/api/v1/upload", json=image1)

# print(resp.json())

import requests

# Mengganti URL_API dengan URL sebenarnya dari API Flask Anda
URL_API = 'http://localhost:5000/api/v1/upload'

# Path file gambar yang akan diunggah
image_path = "D:\Backup\orang.jpg"

# Menguji koneksi ke GCS menggunakan metode GET
# response_get = requests.get(URL_API)
# print(response_get.json())

# Mengunggah gambar ke GCS menggunakan metode POST
files = {'image': open(image_path, 'rb')}
response_post = requests.post(URL_API, files=files)
print(response_post.json())
