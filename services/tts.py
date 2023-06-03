from elevenlabslib import *


class TTS():
    """This is used for text to speech
    """
    def __init__(self, api_key, voice="Meta Akhil") -> None:
        self.user = ElevenLabsUser(api_key)
        self.voice = self.user.get_voices_by_name(voice)[0]  # This is a list because multiple voices can have the same name

    def generate_save_audio(self, prompt, filename):
        data = self.voice.generate_audio(prompt=prompt)
        with open(f'./data/{filename}.wav', mode='bx') as f:
            f.write(data[0])