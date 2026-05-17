from core.engine import VoiceEngine
from core.listener import AudioListener
from core.speaker import VoiceSynthesizer
from core.brain import AssistantBrain
import os
import time

def run_system():
    # 1. Initialize Components
    engine = VoiceEngine()
    listener = AudioListener()
    speaker = VoiceSynthesizer()
    brain = AssistantBrain()
    
    # 2. System State Management
    is_awake = False  # Jarvis starts in Standby Mode
    WAKE_WORDS = ["jarvis", "hey jarvis", "wake up", "wake up jarvis", "good morning"]
    SLEEP_WORDS = ["go to sleep", "standby", "mute", "good night"]
    KILL_WORDS = ["power down", "shut down", "terminate session"]
    
    print("\n=======================================")
    print("      SYSTEM ONLINE - STANDBY MODE      ")
    print("=======================================")
    print("Systems online. Standing by for wake word, Sir.")

    # 3. The Continuous Event Loop
    try:
        while True:
            # Change console prompt based on system state
            if is_awake:
                print("\n[ACTIVE] Listening for command...")
            else:
                print("\n[PASSIVE] Waiting for wake word...")
                
            audio_path = listener.listen_and_record()
            text = engine.transcribe(audio_path)
            
            if text:
                command = text.lower()
                print(f"[USER] >> {text}")
                
                # --- COMMAND TIER 1: The Kill Switch (Always listening) ---
                if any(word in command for word in KILL_WORDS):
                    print("[SYSTEM] Executing shutdown sequence.")
                    speaker.speak("Powering down all systems. Goodbye, Sir.")
                    safe_delete(audio_path)
                    break
                
                # --- COMMAND TIER 2: Sleep Command ---
                if is_awake and any(word in command for word in SLEEP_WORDS):
                    is_awake = False
                    print("[SYSTEM] Entering Standby Mode.")
                    speaker.speak("Entering standby mode. I will be listening if you need me.")
                    safe_delete(audio_path)
                    continue
                
                # --- COMMAND TIER 3: Wake Command ---
                if not is_awake:
                    if any(word in command for word in WAKE_WORDS):
                        is_awake = True
                        print("[SYSTEM] System Awakened.")
                        speaker.speak("Online and ready, Sir.")
                    else:
                        print("[SYSTEM] (Audio ignored - System in Standby)")
                    
                    safe_delete(audio_path)
                    continue # Skip sending audio to the brain
                
                # --- COMMAND TIER 4: Active Cognitive Processing ---
                if is_awake:
                    intelligent_response = brain.think(text)
                    speaker.speak(intelligent_response)
                
            else:
                print("[SYSTEM] (Audio discarded - No speech detected)")
                
            # Clean up buffer after every loop
            safe_delete(audio_path)

    except KeyboardInterrupt:
        print("\n[SYSTEM] Manual override triggered. Shutting down.")
        speaker.speak("Manual shutdown sequence initiated.")

def safe_delete(filepath: str):
    """Safely deletes the temporary audio file without crashing if Windows locks it."""
    if filepath and os.path.exists(filepath):
        try:
            os.remove(filepath)
        except PermissionError:
            # If the file is locked, wait a fraction of a second and try one more time
            time.sleep(0.1)
            try:
                os.remove(filepath)
            except Exception as e:
                print(f"[WARNING] Could not delete temp file: {e}")

if __name__ == "__main__":
    run_system()