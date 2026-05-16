import speech_recognition as sr
import os
from config import AUDIO_BUFFER_DIR

class AudioListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Optimize threshold settings for faster cut-off
        self.recognizer.pause_threshold = 0.8 # Seconds of silence before cutting the recording
        
        print("[SYSTEM] Calibrating microphone to ambient noise floor...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
        print("[SYSTEM] Microphone calibrated.")

    def listen_and_record(self) -> str:
        """Listens continuously until speech is detected, saves it, and returns the filepath."""
        temp_file_path = os.path.join(AUDIO_BUFFER_DIR, "temp_chunk.wav")
        
        with self.microphone as source:
            print("\n[LISTENING] ...")
            # This will block/wait indefinitely until it hears a voice
            audio_data = self.recognizer.listen(source)
            
            print("[PROCESSING] Voice detected, handing off to GPU...")
            
            # Save the captured audio block to the buffer
            with open(temp_file_path, "wb") as f:
                f.write(audio_data.get_wav_data())
                
        return temp_file_path