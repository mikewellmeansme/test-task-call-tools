from pydub import AudioSegment
from logger import logger


class AudioManager:
    _audio : AudioSegment
    _path_to_wav: str

    def __init__(self, path_to_wav: str) -> None:

        if not path_to_wav.endswith('.wav'):
            raise NotImplementedError('AudioManager supports only .wav files!')
        
        self._path_to_wav = path_to_wav
        self._audio = AudioSegment.from_wav(path_to_wav)

    @logger
    def change_speed(self, speed: float) -> None:

        # BUG: Питчит звук

        temp_audio = self._audio._spawn(
            self._audio.raw_data,
            overrides={"frame_rate": int(self._audio.frame_rate * speed)}
        )
        self._audio = temp_audio.set_frame_rate(self._audio.frame_rate)

    
    @logger
    def change_volume(self, db_to_add: float) -> None:
        self._audio = self._audio + db_to_add
    
    @logger
    def export(self, path: str)  -> None:
        self._audio.export(path, format="wav")

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._path_to_wav})'
