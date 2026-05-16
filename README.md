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

