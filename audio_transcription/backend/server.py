from ..ml.model import AudioTranscriptionModel
from flask_ml.flask_ml_server import MLServer
from flask_ml.flask_ml_server.constants import DataTypes
from flask_ml.flask_ml_server.models import BatchTextResult, TextInput, TextResult

model = AudioTranscriptionModel()
server = MLServer(__name__)

@server.route('/transcribe', input_type=DataTypes.AUDIO)
def transcribe(inputs: list[TextInput], parameters: dict) -> BatchTextResult:
    print('Inputs:', inputs)
    print('Parameters:', parameters)
    files = [e.file_path for e in inputs]
    results = model.transcribe_batch(files)
    results = [TextResult(id=e["file_path"], result=e["result"]) for e in results]
    results = BatchTextResult(results=results)
    return results

server.run()