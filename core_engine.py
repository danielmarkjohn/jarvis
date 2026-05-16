import os
import sys

# 1. Locate the exact folders where pip installed the NVIDIA binaries
site_packages = os.path.join(sys.prefix, "Lib", "site-packages")
cublas_bin = os.path.join(site_packages, "nvidia", "cublas", "bin")
cudnn_bin = os.path.join(site_packages, "nvidia", "cudnn", "bin")

# 2. BRUTE FORCE: Inject these paths directly into the Windows PATH environment variable
# This forces the CTranslate2 C++ engine to see the DLLs
os.environ["PATH"] = f"{cublas_bin};{cudnn_bin};" + os.environ.get("PATH", "")

# 3. Keep the Python-level registration just as a safety net
if os.path.exists(cublas_bin): 
    os.add_dll_directory(cublas_bin)
if os.path.exists(cudnn_bin): 
    os.add_dll_directory(cudnn_bin)

# 4. NOW import the model (it will check the PATH as it loads)
from faster_whisper import WhisperModel
import time

# Configuration
MODEL_SIZE = "small" 
DEVICE = "cuda"
COMPUTE_TYPE = "float16" 

def main():
    print(f"Loading '{MODEL_SIZE}' model into VRAM...")
    
    # Initialize the model
    model = WhisperModel(MODEL_SIZE, device=DEVICE, compute_type=COMPUTE_TYPE)
    print("Model loaded successfully. GPU Engine is running.")

    audio_file = "test.wav" # Ensure this matches your file name
    
    print(f"Transcribing {audio_file}...")
    start_time = time.time()
    
    # Run transcription
    segments, info = model.transcribe(audio_file, beam_size=5)

    print(f"Detected language: {info.language} (Probability: {info.language_probability:.2f})")
    
    print("\n--- Transcription ---")
    for segment in segments:
        print(f"[{segment.start:.2f}s -> {segment.end:.2f}s] {segment.text}")
        
    print(f"\nTime taken: {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()