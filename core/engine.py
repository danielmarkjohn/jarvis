import os
import sys
import time
from config import MODEL_SIZE, DEVICE, COMPUTE_TYPE

# BRUTE FORCE CUDA PATH INJECTION
site_packages = os.path.join(sys.prefix, "Lib", "site-packages")
cublas_bin = os.path.join(site_packages, "nvidia", "cublas", "bin")
cudnn_bin = os.path.join(site_packages, "nvidia", "cudnn", "bin")
os.environ["PATH"] = f"{cublas_bin};{cudnn_bin};" + os.environ.get("PATH", "")

from faster_whisper import WhisperModel

class VoiceEngine:
    def __init__(self):
        print(f"[SYSTEM] Booting AI Engine. Loading '{MODEL_SIZE}' model into VRAM...")
        self.model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type=COMPUTE_TYPE)
        print("[SYSTEM] VRAM populated. Engine is hot.")

    def transcribe(self, audio_path: str) -> str:
        """Processes the audio chunk and returns the transcribed text."""
        segments, info = self.model.transcribe(audio_path, beam_size=5)
        
        # Combine all segments into a single string
        transcription = "".join([segment.text for segment in segments])
        return transcription.strip()