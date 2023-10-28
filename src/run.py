import typer

from audio_manager import AudioManager
from speech_recognizer import SpeechRecognizer


app = typer.Typer()

@app.command()
def change_speed(path: str, speed: float):
    """
    Changes the speed of the specified file by the specified rate.

    path: path to the .WAV file

    speed: rate

    Example: change-speed audio/1.wav 1.5
    """
    am = AudioManager(path)
    am.change_speed(speed)
    am.export(
        f"{path.removesuffix('.wav')}"
        f"_speed_x{speed}.wav"
    )

@app.command()
def change_volume(path: str, volume: float):
    """
    Changes the volume of the specified file by the specified number of decibels.

    path: path to the .WAV file

    volume: decibels to add to the volume

    For the negative values use -- value

    Example: change-volume audio/1.wav -- -20
    """
    am = AudioManager(path)
    am.change_volume(volume)
    am.export(
        f"{path.removesuffix('.wav')}"
        f"_volume_{'+' if volume > 0 else ''}"
        f"{volume}.wav"
    )

@app.command()
def recognize(path: str):
    sr = SpeechRecognizer('base')
    text = sr.recognize(path)
    print(text)


if __name__ == "__main__":
    app()
