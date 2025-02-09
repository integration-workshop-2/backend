from gtts import gTTS
from pathlib import Path
from playsound import playsound
from uuid import uuid4


class SpeakerUtil:
    def __init__(self) -> None:
        self.__audio_folder = (
            Path(__file__).resolve().parent.parent.parent.parent / "audio_data"
        )

        self.__audio_folder.mkdir(parents=True, exist_ok=True)

    def speak(self, text: str) -> None:
        filename = self.__audio_folder / f"{str(uuid4())}.mp3"
        tts = gTTS(text=text, lang="pt")
        tts.save(filename)
        playsound(str(filename))
        filename.unlink()
