# Real-time in-browser transcription

## Installation
- install python and pip
- pip install -r requirements.txt [macOs requires portaudio for pyAudio]

MAC
$ git clone https://github.com/Tancre/stt && cd stt [git clone https://github.com/Tancre/stt; cd stt]
$ python3 -m venv .venv && source .venv/bin/activate [python3 -m venv .venv; ./.venv/Scripts/activate]
$ make

--- makefile
default: server

install:
	@python3 -m venv .venv && .venv/bin/pip install -r requirements.txt   [python3 -m venv .venv; ./.venv/Scripts/pip install -r requirements]

server:
	@.venv/bin/python3 app.py [./.venv/Scripts/python.exe app.py]
    sensible-browser index.html [Start-Process "https://debug.to"]

.PHONY: install server
---


## Find and set input device index
- run script find_input_device_index.py [it can help to check the audio settings for the name of the device]
- change input device index in app.py

## Run 
- run app.py [the model is loaded at first run]
- open index.html

## Settings
- framerate
- seconds recording
- buffer

## Debug
- check browser's console to understand if the connection was succeful
- check output app.py for errors

WINDOWS DEBUG

----------------------------------------------------------
error: running scripts is disabled on this system"
----------------------------------------------------------
1. First, Open PowerShell with Run as Administrator.
2. Then, run this command in PowerShell
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
3. After that type Y and press Enter.
----------------------------------------------------------

install python3 >> microsoft store >> python3
install chocolately >> https://chocolatey.org/install
install make

----------------------------------------------------------
