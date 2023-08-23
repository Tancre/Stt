# Install pyaudio from http://people.csail.mit.edu/hubert/pyaudio/
# Find audio device index using this code
import pyaudio, time, json

p = pyaudio.PyAudio()
for i in range(p.get_device_count()):
    print("[" + p.get_device_info_by_index(i)["index"] + "]", p.get_device_info_by_index(i)["name"])

time.sleep(60000)
p.terminate()