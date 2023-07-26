# Real-time in-browser transcription

## Installatio

## Mac & Linux
- requirements: git, python, make, portaudio (only mac), python3-pyaudio (only linux)
$ git clone https://github.com/Tancre/stt && cd stt
$ make install-mac

### Windows
- requirements: git, python, make (install with chocolately)
$ git clone https://github.com/Tancre/stt; cd stt
$ make install-windows

## Setup: Find and set input device index
$ make find-device
open app.py and change input device index on line 16

## Run 
$ make

## Settings
- framerate
- seconds recording
- buffer

## Debug
- check browser's console to understand if the connection was succeful
- check output app.py for errors

### WINDOWS DEBUG

- error: running scripts is disabled on this system
1. First, Open PowerShell with Run as Administrator.
2. Then, run this command in PowerShell
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
3. After that type Y and press Enter.