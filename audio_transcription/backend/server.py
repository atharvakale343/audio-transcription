from ..ml.model import AudioTranscriptionModel
from flask_ml.flask_ml_server import MLServer
from flask_ml.flask_ml_server.constants import DataTypes
from flask_ml.flask_ml_server.models import FileInput, ImageResult, ResponseModel, TextInput, TextResult

model = AudioTranscriptionModel()
server = MLServer(__name__)

@server.route('/transcribe', input_type=DataTypes.AUDIO)
def transcribe(inputs: list[dict], parameters: dict):
    print('Inputs:', inputs)
    print('Parameters:', parameters)
    files = [e['file_path'] for e in inputs]
    results = model.transcribe_batch(files)
    results = [TextResult(text=e["file_path"], result=e["result"]) for e in results]
    response = ResponseModel(results=results)
    return response.get_response()

server.run()