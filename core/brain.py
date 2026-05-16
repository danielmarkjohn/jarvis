import ollama
from config import LLM_MODEL, SYSTEM_PROMPT

class AssistantBrain:
    def __init__(self):
        print(f"[SYSTEM] Booting Cognitive Engine ({LLM_MODEL})...")
        self.model = LLM_MODEL
        self.system_prompt = SYSTEM_PROMPT
        print("[SYSTEM] Cognitive Engine is online.")

    def think(self, user_input: str) -> str:
        """Sends transcribed text to Llama 3 and returns the response."""
        try:
            print("[PROCESSING] Consulting LLM...")
            response = ollama.chat(model=self.model, messages=[
                {'role': 'system', 'content': self.system_prompt},
                {'role': 'user', 'content': user_input}
            ])
            
            # Extract the text
            answer = response['message']['content']
            return answer.strip()
            
        except Exception as e:
            print(f"[ERROR] Brain offline: {e}")
            return "I am currently disconnected from my cognitive framework, sir."