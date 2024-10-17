from flask_ml.flask_ml_client import MLClient

url = "http://127.0.0.1:5000/transcribe"  # The URL of the server
client = MLClient(url)  # Create an instance of the MLClient object

inputs = [
    {"file_path": "audio.mp3"},
]  # The inputs to be sent to the server

inputs = {"audio_files": {"files": [{"path": "audio.mp3"}]}}

parameters = {}


response = client.request(inputs, parameters)  # Send a request to the server
print(response)  # Print the response
