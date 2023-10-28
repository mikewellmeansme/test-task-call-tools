import whisper
from logger import logger


class SpeechRecognizer:
    _model: whisper.Whisper
    
    def __init__(self, model_name: str, **model_kwargs) -> None:
        self._model = whisper.load_model(model_name, **model_kwargs)

    @logger
    def recognize(self, path_to_wav: str) -> str:
        result = self._model.transcribe(path_to_wav)
        return result['text']
    
    def __repr__(self) -> str:
        return self.__class__.__name__
