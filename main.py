from core.engine import VoiceEngine
from core.listener import AudioListener
from core.speaker import VoiceSynthesizer
from core.brain import AssistantBrain
import os

def run_system():
    # 1. Initialize all components
    engine = VoiceEngine()       # The Ears (Whisper)
    listener = AudioListener()   # The Microphone hook
    speaker = VoiceSynthesizer() # The Mouth (TTS)
    brain = AssistantBrain()     # The Brain (Ollama)
    
    print("\n=======================================")
    print("      SYSTEM ONLINE - AUTO-ON MODE      ")
    print("=======================================")

    # 2. Boot sequence
    speaker.speak("All systems are online and fully operational.")

    # 3. Start the continuous event loop
    try:
        while True:
            # Block and wait for user to speak
            audio_path = listener.listen_and_record()
            
            # Step A: Ears (Transcribe the audio)
            text = engine.transcribe(audio_path)
            
            if text:
                print(f"\n[USER] >> {text}")
                
                # Step B: Brain (Generate an intelligent response)
                intelligent_response = brain.think(text)
                
                # Step C: Mouth (Speak the response out loud)
                speaker.speak(intelligent_response)
                
            else:
                print("[SYSTEM] (Audio discarded - no speech detected)")
                
            # Clean up the temporary audio buffer file
            if os.path.exists(audio_path):
                os.remove(audio_path)

    except KeyboardInterrupt:
        print("\n[SYSTEM] Shutting down continuous listening mode.")
        speaker.speak("Powering down system. Goodbye.")

if __name__ == "__main__":
    run_system()