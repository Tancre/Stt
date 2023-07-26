# Real-time in-browser transcription

## Installation

### Mac & Linux
Requirements: git, python, make, portaudio (only mac), python3-pyaudio (only linux)
<code>$ git clone https://github.com/Tancre/stt && cd stt
$ make install-mac
</code>

### Windows
Requirements: git, python, make (install with chocolately)
<code>$ git clone https://github.com/Tancre/stt; cd stt 
$ make install-windows</code>

## Setup: Find and set input device index
<code>$ make find-device</code>
- Open app.py and change input device index number on line 16

## Run 
<code>$ make</code>

## Settings
- framerate
- seconds recording
- buffer

## Debug
- check browser's console to understand if the connection was succeful
- check output app.py for errors

### Windows

- error: running scripts is disabled on this system
1. First, Open PowerShell with Run as Administrator.
2. Then, run this command in PowerShell
	Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
3. After that type Y and press Enter.