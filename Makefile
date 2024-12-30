
# Makefile for building a PyInstaller executable

# Variables
PYINSTALLER=pyinstaller
SCRIPT=telegram-cli.py
OUTPUT_DIR=dist
HIDDEN_IMPORTS=--hidden-import=pyasn1 --hidden-import=rsa --hidden-import=Telethon --hidden-import=pyaes
EXTRA_BINARY=--add-binary '/usr/lib/libstdc++.so.6:.'
OPTIONS=--onefile --strip --noconsole --clean

# Default target
.PHONY: all
all: build

# Build target
.PHONY: build
build:
	$(PYINSTALLER) $(OPTIONS) $(HIDDEN_IMPORTS) $(EXTRA_BINARY) $(SCRIPT)

# Clean target
.PHONY: clean
clean:
	rm -rf $(OUTPUT_DIR) build *.spec __pycache__
