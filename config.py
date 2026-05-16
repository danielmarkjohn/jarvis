import os

# --- Hardware & Model Settings ---
MODEL_SIZE = "small"
DEVICE = "cuda"
COMPUTE_TYPE = "float16"

# --- Directory Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_BUFFER_DIR = os.path.join(BASE_DIR, "audio_buffer")

# Ensure the temporary audio buffer folder exists
os.makedirs(AUDIO_BUFFER_DIR, exist_ok=True)