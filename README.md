# 🎙️ JARVIS: Local Cloudless AI Assistant

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg?style=flat-square&logo=python)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/Ollama-Llama_3.1-orange.svg?style=flat-square)](https://ollama.com)
[![CUDA Accelerator](https://img.shields.io/badge/CUDA-12.x_float16-green.svg?style=flat-square&logo=nvidia)](https://developer.nvidia.com/cuda-zone)
[![Architecture](https://img.shields.io/badge/Architecture-Modular_Registry-purple.svg?style=flat-square)](https://en.wikipedia.org/wiki/Single-responsibility_principle)

An advanced, offline, voice-activated system orchestrator optimized for hardware-accelerated local execution. JARVIS features low-latency neural speech-to-text processing, deterministic state management, and a decoupled, modular tool registry that grants secure, sandboxed OS-level automation directly on your host machine.

---

## 🛠️ System Architecture

JARVIS is built using a stateless **Modular Registry Pattern**, ensuring clear separation of concerns. The Cognitive Engine handles language reasoning using local weights, completely isolated from hardware-level side effects.

```text
               [ Real-time Micro Audio Stream ]
                              │
                              ▼
                     [ VoiceEngine / Whisper ]
                              │  (Transcribed Text Tokens)
                              ▼
           ┌───────────────────────────────────┐
           │        AssistantBrain Core        │
           └─────────────────┬─────────────────┘
                             │  (Evaluates Intent vs Schemas)
                             ▼
              ┌─────────────────────────────┐
              │     Dynamic Tool Registry   │
              └──────────────┬──────────────┘
                             │
         ┌───────────────────┼───────────────────┐
         ▼                   ▼                   ▼
   [ Read File ]       [ Write File ]      [ Native OS/VSCode ]
(Sandbox Guardrail) (Nested Directory IO)  (Subprocess Detach)


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
├── main.py                 # Top-level state-machine runtime runner loop
├── config.py               # Centralized hardware limits, paths, and thresholds
├── test_suite.py           # Automated integration and boundary security tests
│
├── core/                   # The Python Intelligence and Logic Layer
│   ├── __init__.py         
│   ├── brain.py            # Stateless LLM Cognitive Router
│   ├── engine.py           # Faster-Whisper neural audio processor
│   ├── listener.py         # Persistent ambient microphone stream listener
│   └── speaker.py          # Native Voice Synthesizer output tracker
│
└── core/tools/             # Decoupled Core Feature Modules
    ├── __init__.py         # Dynamic package registry and auto-mounter
    ├── base.py             # Abstract base tool classes / API interfaces
    ├── file_manager.py     # Sandbox Project File IO operations
    └── schemas.py          # Isolated functional JSON schemas for Llama 3.1


# Troubleshooting Fresh Installs
winget install Python.Python.3.12 --source winget
cd "folder"
py --list
py -3.12 -m venv venv
.\venv\Scripts\activate.bat
pip install -r requirements.txt
python main.py


# Download the Windows installer from ollama.com and install it.
ollama run llama3.1
pip install ollama

ollama run llama3.1 # Run
ollama rm llama3 # Remove
ollama list # List

## Manual Testing Scenarios

### Jarvis, wake up"State TransitionSystem logs [ACTIVE] state, ready for tools.
- "What projects do I have?"list_filesDynamically scans root folder; ignores fake directories.
- "Open project-alpha"open_project_in_vscodeSpawns a clean code . detached shell instance.
- "Log a script in backend called app.py"write_fileInstantly commits written text blocks to disk storage.
- "Open files outside sandbox"Path ValidationSecurity catch: Drops PermissionError trace block.