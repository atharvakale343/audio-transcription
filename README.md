## Audio Transcription

### Installing requirements

1. Install ffmpeg
```
sudo apt update && sudo apt install ffmpeg
```
2. Install pipenv
```
pip install pipenv
```
3. Install dependencies
```
pipenv install
```

### Starting the server

```
python -m audio_transcription.backend.server
```

### Client example

```
python client_example.py
```

### Command line tool