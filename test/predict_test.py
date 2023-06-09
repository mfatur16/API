import requests
from flask import jsonify
import json

input1 = {
        "gender": "Men",
        "usage": "Casual",
        "baseColour": "Blue"
    }

headers = {
    "Content-Type": "application/json"
}

# resp = requests.post("https://backend-emvqwfvxaa-et.a.run.app/api/v1/predict", json=input1, headers=headers)

# print(resp.json())

payload = json.dumps(input1, indent=4)

resp = requests.post("https://backend-emvqwfvxaa-et.a.run.app/api/v1/predict", data=payload, headers=headers)
result = resp.json()
result_str = json.dumps(result, indent=4)

print(result_str)