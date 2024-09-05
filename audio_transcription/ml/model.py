import whisper


class AudioTranscriptionModel:
    def __init__(self, model_path: str="base"):
        self.model = whisper.load_model(model_path)

    def _validate_audio_path(self, audio_path: str) -> None:
        if audio_path is None:
            raise ValueError("audio_path cannot be None")

    def transcribe(self, audio_path: str) -> str:
        self._validate_audio_path(audio_path)
        return self.model.transcribe(audio_path)["text"]
