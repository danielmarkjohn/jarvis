# Local AI Assistant - Core Engine Setup

This guide covers the initial setup for the local voice recognition pipeline using `faster-whisper`. The configuration is optimized for local GPU execution (CUDA, float16).

## Prerequisites

* Windows 11 Pro
* Python 3.10 or 3.11 installed
* NVIDIA GPU (RTX 40-series) with updated drivers

## Phase 1: System Dependencies

`faster-whisper` requires FFmpeg to process audio files and streams. On Windows 11, you can install this easily via the Windows Package Manager (`winget`) or by downloading the binaries.

**Open Command Prompt or PowerShell as Administrator and run:**

```bash
# Install FFmpeg using winget
winget install Gyan.FFmpeg


# If That doesnt work!
winget source update
winget install Gyan.FFmpeg

# 1. Create a virtual environment (optional but recommended)
python -m venv jarvis

# 2. Activate the virtual environment
# On Windows Command Prompt:
jarvis\Scripts\activate.bat
# On PowerShell:
.\jarvis\Scripts\Activate.ps1

# 3. Install the primary speech recognition library
pip install faster-whisper

# Running Scripts
Scripts\activate.bat

# Confirm
where python

# Launch
python core_engine.py

# IF Fails Install NVIDIA Lib
pip install nvidia-cublas-cu12 nvidia-cudnn-cu12

# Proposed Folder Structure
jarvis/
│
├── venv/                   # (Already exists - Python sandbox)
├── audio_buffer/           # Temporary holding zone for live microphone chunks
├── storage/                # The local vault for your project management system
│
├── core/                   # The Python intelligence and logic layer
│   ├── __init__.py         
│   ├── engine.py           
│   ├── listener.py         
│   └── intent_parser.py    
│
├── ui/                     # Future home for the Electron/React visualization app
│
├── main.py                 
├── config.py               
└── requirements.txt

# Troubleshooting Fresh Installs
winget install Python.Python.3.12 --source winget
cd "folder"
py --list
py -3.12 -m venv venv
.\venv\Scripts\activate.bat
pip install -r requirements.txt
python main.py


# Download the Windows installer from ollama.com and install it.
ollama run llama3
pip install ollama
