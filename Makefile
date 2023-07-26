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
	./.venv/Scripts/activate
	python.exe app.py

.PHONY: install server activate