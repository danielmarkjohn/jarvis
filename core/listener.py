import speech_recognition as sr
import os
from config import AUDIO_BUFFER_DIR, MIC_PAUSE_THRESHOLD, MIC_ENERGY_THRESHOLD

class AudioListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # --- THE TIMING & TRIGGER FIX ---
        self.recognizer.pause_threshold = MIC_PAUSE_THRESHOLD
        self.recognizer.energy_threshold = MIC_ENERGY_THRESHOLD
        
        # CRITICAL: Turn off dynamic adjustment so it stops picking up AC/fans/keyboard clicks
        self.recognizer.dynamic_energy_threshold = False 
        
        print("[SYSTEM] Calibrating microphone (Dynamic Sensitivity OFF)...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
        print("[SYSTEM] Microphone locked and calibrated.")

    def listen_and_record(self) -> str:
        temp_file_path = os.path.join(AUDIO_BUFFER_DIR, "temp_chunk.wav")
        with self.microphone as source:
            print("\n[LISTENING] ...")
            try:
                # Add a timeout so it doesn't get stuck listening to static forever
                audio_data = self.recognizer.listen(source, timeout=None, phrase_time_limit=15)
                
                print("[PROCESSING] Voice detected, handing off to GPU...")
                with open(temp_file_path, "wb") as f:
                    f.write(audio_data.get_wav_data())
                return temp_file_path
            
            except sr.WaitTimeoutError:
                return None