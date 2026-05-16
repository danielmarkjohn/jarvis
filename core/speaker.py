import pyttsx3

class VoiceSynthesizer:
    def __init__(self):
        print("[SYSTEM] Initializing Text-to-Speech engine...")
        self.engine = pyttsx3.init()
        
        # --- Configuration ---
        self.engine.setProperty('rate', 175)    # Speed of speech (words per minute)
        self.engine.setProperty('volume', 1.0)  # Volume level (0.0 to 1.0)
        
        # Optional: Change the voice
        # Windows usually has a male (0) and a female (1) voice installed by default
        voices = self.engine.getProperty('voices')
        if len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id) 

        print("[SYSTEM] Voice module loaded.")

    def speak(self, text: str):
        """Converts text to audio and plays it through the default speakers."""
        if text:
            print(f"[JARVIS] << {text}")
            self.engine.say(text)
            # This command blocks the script while the audio is playing so it doesn't overlap
            self.engine.runAndWait()