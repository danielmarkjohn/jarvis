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
# The System Prompt dictates Jarvis's personality. 
SYSTEM_PROMPT = """You are Jarvis, a highly efficient, witty, and concise AI assistant. 
Keep all responses conversational, professional, and strictly under 3 sentences. 
Do not use emojis, markdown, or lists, as your text will be read aloud by a voice synthesizer."""

# --- Speaker (TTS) Settings ---
TTS_RATE = 175       # 175 is slightly brisk and efficient. Default is 200.
TTS_VOLUME = 1.0     # Max volume