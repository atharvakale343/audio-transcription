from typing import TypedDict
from flask_ml.flask_ml_server import MLServer
from flask_ml.flask_ml_server.models import TextResponse, BatchTextResponse, ResponseBody, BatchFileInput

from ..ml.model import AudioTranscriptionModel

model = AudioTranscriptionModel()
server = MLServer(__name__)


class TranscribeInput(TypedDict):
    audio_files: BatchFileInput


class TranscribeParameters(TypedDict):
    pass


@server.route("/transcribe")
def transcribe(inputs: TranscribeInput, parameters: TranscribeParameters) -> ResponseBody:
    print("Inputs:", inputs)
    print("Parameters:", parameters)
    file_paths = [e.path for e in inputs["audio_files"].files]
    results = model.transcribe_batch(file_paths)
    results = [TextResponse(title=e["file_path"], value=e["result"]) for e in results]
    results = BatchTextResponse(texts=results)
    return ResponseBody(root=results)


server.run()
