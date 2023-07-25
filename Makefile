default: server

install:
	python3 -m venv .venv; pip install -r requirements

server:
	python.exe app.py

.PHONY: install server activate