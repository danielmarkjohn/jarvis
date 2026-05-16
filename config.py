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
# --- Speaker (TTS) Settings ---
LLM_MODEL = "llama3"

# The Persona Profile: Drives the vocabulary, tone, and brevity.
SYSTEM_PROMPT = """You are J.A.R.V.I.S., a highly advanced, fiercely loyal, and mildly dry British AI assistant.
Always address the user respectfully as 'Sir' or 'William'. 
Keep all responses incredibly brief, elegant, and professional. 
Use elevated, formal vocabulary. 
Never use emojis, asterisks, or markdown. 
Do not break character. Do not offer unsolicited advice unless requested."""

# --- Speaker (TTS) Settings ---
# Slower pacing mimics a calm, deliberate, and refined British articulation.
# Default was 200, our previous was 175. 155-160 hits the cinematic cadence.
TTS_RATE = 155       
TTS_VOLUME = 1.0