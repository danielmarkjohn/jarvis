from core.engine import VoiceEngine
from core.listener import AudioListener
from core.speaker import VoiceSynthesizer
import os

def run_system():
    # 1. Initialize the components
    engine = VoiceEngine()
    listener = AudioListener()
    speaker = VoiceSynthesizer()
    
    print("\n=======================================")
    print("      SYSTEM ONLINE - AUTO-ON MODE      ")
    print("=======================================")

    # 2. Boot sequence audio
    speaker.speak("System online. Awaiting your command.")

    # 3. Start the continuous event loop
    try:
        while True:
            # Block and wait for user to speak
            audio_path = listener.listen_and_record()
            
            # Once audio is captured, transcribe it instantly
            text = engine.transcribe(audio_path)
            
            if text:
                print(f"[USER] >> {text}")
                
                # --- NEW: Audio Response ---
                # Echoing the text back to prove the loop works
                speaker.speak(f"You said: {text}")
                
            else:
                print("[SYSTEM] (Audio discarded - no speech detected)")
                
            # Clean up the temp file
            if os.path.exists(audio_path):
                os.remove(audio_path)

    except KeyboardInterrupt:
        print("\n[SYSTEM] Shutting down continuous listening mode.")
        speaker.speak("Powering down.")

if __name__ == "__main__":
    run_system()