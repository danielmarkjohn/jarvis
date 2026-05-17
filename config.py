import os

# --- Hardware & Whisper Settings ---
MODEL_SIZE = "small"
DEVICE = "cuda"
COMPUTE_TYPE = "float16"

# --- Directory Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_BUFFER_DIR = os.path.join(BASE_DIR, "audio_buffer")
os.makedirs(AUDIO_BUFFER_DIR, exist_ok=True)

# --- Brain (LLM) Settings ---
LLM_MODEL = "llama3"
SYSTEM_PROMPT = """You are JARVIS, a highly advanced, fiercely loyal, and mildly dry British AI assistant.
Always address the user respectfully as 'Sir' or 'Daniel'. 
Keep all responses incredibly brief, elegant, and professional. 
Never use emojis, asterisks, or markdown. Do not break character."""

# --- Speaker (TTS) Settings ---
TTS_RATE = 155       
TTS_VOLUME = 1.0     

# --- NEW: Microphone & Timing Settings ---
# Increase to 1.5 or 2.0 if Jarvis cuts you off while you are thinking/breathing.
# Decrease to 0.8 if Jarvis waits too long to reply after you finish speaking.
MIC_PAUSE_THRESHOLD = 1.2 

# Hard volume floor. Increase this (e.g., 500, 800) if background noise causes random triggers.
MIC_ENERGY_THRESHOLD = 400