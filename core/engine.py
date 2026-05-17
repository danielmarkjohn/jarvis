import os
import sys
from config import MODEL_SIZE, DEVICE, COMPUTE_TYPE

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
        if not audio_path or not os.path.exists(audio_path):
            return ""

        # vad_filter=True automatically drops dead silence and static
        segments_generator, info = self.model.transcribe(audio_path, beam_size=5, vad_filter=True)
        
        # Convert the generator into a list so we can actually read the text
        segments = list(segments_generator)
        
        # If the VAD filter stripped everything out, return empty
        if not segments:
            return ""
            
        transcription = "".join([segment.text for segment in segments]).strip()
        
        # The Hallucination Blacklist: Filter out phantom text caused by mic static
        hallucinations = [
            "Thank you.", "Thank you", "You", ".", "Subscribe.", 
            "Amara.org", "Thank you for watching.", "Thanks for watching!"
        ]
        
        if transcription in hallucinations or len(transcription) < 2:
            return ""
            
        return transcription