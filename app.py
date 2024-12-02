from openai import OpenAI
from utils import record_audio, play_audio

client = OpenAI()

record_audio('test.wav')
audio_file = open('test.wav', 'rb')
transcription = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file
)

print(transcription.text)
