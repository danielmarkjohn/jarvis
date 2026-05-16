@echo off
title Jarvis AI Core Environment
echo Initiating Jarvis Startup Sequence...

:: Navigate exactly to your project directory
cd /d "C:\AAA_Codespace\Project Hail Mary\jarvis"

:: Activate the Python 3.12 sandbox
call venv\Scripts\activate.bat

:: Launch the orchestrator
python main.py

:: Keep the window open if the system crashes
pause