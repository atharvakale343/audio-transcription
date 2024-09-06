from flask_ml.flask_ml_client import MLClient
from flask_ml.flask_ml_server.constants import DataTypes

url = 'http://127.0.0.1:5000/transcribe'  # The URL of the server
client = MLClient(url)  # Create an instance of the MLClient object

inputs = [
    {'file_path': 'audio.mp3'},
]  # The inputs to be sent to the server
data_type = DataTypes.AUDIO  # The type of the input data

response = client.request(inputs, data_type)  # Send a request to the server
print(response)  # Print the response