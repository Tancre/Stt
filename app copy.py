import pyaudio
import json
from vosk import Model, KaldiRecognizer
from threading import Thread
import subprocess
from queue import Queue
import time
import asyncio
import websockets
import pathlib
import webbrowser

path_html = str(pathlib.Path(__file__).parent.absolute()) + "\index.html"

INPUT_DEVICE_INDEX = 1
FRAME_RATE = 32000
RECORD_SECONDS = 3
CHUNK = 8192

CHANNELS = 1
AUDIO_FORMAT = pyaudio.paInt16
SAMPLE_SIZE = 2

recordings = Queue()

model = Model(model_name="vosk-model-it-0.22")
rec = KaldiRecognizer(model, FRAME_RATE)
rec.SetWords(True)

p = pyaudio.PyAudio()
stream = p.open(format = AUDIO_FORMAT,
                channels = CHANNELS,
                rate = FRAME_RATE,
                input=True,
                input_device_index=1,
                frames_per_buffer=CHUNK)
stream.start_stream()

transcription = []

class recognition:
    def speech(self):
        self.frames = []
        while True:
            self.data = stream.read(20000)
            self.frames.append(self.data)
            recordings.put(self.frames.copy())
            self.frames = []
        stream.stop_stream()
        stream.close()
        p.terminate
    def transcribe(self):
        while True:
            frames = recordings.get()
            rec.AcceptWaveform(b''.join(frames))
            result = rec.Result()[14:-3]
            # text = json.loads(result)["text"]
            transcription.append(result)
            print(result)
           
async def show_transcription(websocket):
    while True:
        message = transcription[-1]
        await websocket.send(message)
        await asyncio.sleep(5)

async def main():
    async with websockets.serve(show_transcription, "localhost", 5678):
        await asyncio.Future()  # run forever

sr = recognition()
record = Thread(target=sr.speech)
record.start()
time.sleep(2)
transcribe = Thread(target=sr.transcribe)
transcribe.start()
print('\n Starting... \n')
time.sleep(5)
webbrowser.open(path_html)

if __name__ == "__main__":
    asyncio.run(main())
    