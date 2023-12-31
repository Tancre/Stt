default: server

find-device:
	python.exe find_input_device_index.py

install-windows:
	python3 -m venv .venv; ./.venv/Scripts/activate
	pip install -r requirements.txt

install-mac:
	python3 -m venv .venv && source .venv/bin/activate
	pip install -r requirements.txt

server:
	python.exe app.py

.PHONY: install-mac install-windows server find-device