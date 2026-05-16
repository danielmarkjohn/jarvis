import pyttsx3
import re
from config import TTS_RATE, TTS_VOLUME

class VoiceSynthesizer:
    def __init__(self):
        print("[SYSTEM] Voice module loaded (Dynamic Threading Mode).")

    def clean_text(self, text: str) -> str:
        """Strips emojis, asterisks, and markdown that SAPI5 chokes on."""
        # Remove anything between asterisks (e.g., *sighs*)
        text = re.sub(r'\*.*?\*', '', text)
        # Remove standard markdown formatting symbols
        text = text.replace('*', '').replace('#', '').replace('_', '')
        # Remove emojis and keep only standard alphanumeric characters and basic punctuation
        text = re.sub(r'[^\w\s.,!?\'-]', '', text)
        return text.strip()

    def speak(self, text: str):
        """Creates a fresh audio engine for every line to bypass the Windows loop bug."""
        if not text:
            return
            
        clean_response = self.clean_text(text)
        
        # If the LLM only responded with an emoji or action, don't try to speak empty text
        if not clean_response:
            print("[SYSTEM] (Response was only markdown/emojis, skipping audio)")
            return

        print(f"[JARVIS] << {clean_response}")
        
        try:
            # Initialize fresh every time to prevent the 'silent loop' bug
            engine = pyttsx3.init()
            engine.setProperty('rate', TTS_RATE)
            engine.setProperty('volume', TTS_VOLUME)
            
            # Force the most stable default system voice
            voices = engine.getProperty('voices')
            if voices:
                engine.setProperty('voice', voices[0].id)
                
            engine.say(clean_response)
            engine.runAndWait()
            
            # Explicitly destroy the engine to free up the Windows COM thread
            del engine 
            
        except Exception as e:
            print(f"[ERROR] TTS Engine failed to process text: {e}")