import ollama
from config import LLM_MODEL, SYSTEM_PROMPT
from core.tools import registry

class AssistantBrain:
    def __init__(self):
        print(f"[SYSTEM] Booting Modular Cognitive Engine ({LLM_MODEL})...")
        self.model = LLM_MODEL
        self.system_prompt = SYSTEM_PROMPT
        print("[SYSTEM] Cognitive Engine modular sequence is online.")

    def think(self, user_input: str) -> str:
        try:
            print("[PROCESSING] Thinking...")
            messages = [
                {'role': 'system', 'content': self.system_prompt},
                {'role': 'user', 'content': user_input}
            ]
            
            response = ollama.chat(
                model=self.model, 
                messages=messages, 
                tools=registry.get_all_schemas()
            )
            
            if response.get('message', {}).get('tool_calls'):
                messages.append(response['message'])
                
                for tool in response['message']['tool_calls']:
                    function_name = tool['function']['name']
                    arguments = tool['function']['arguments']
                    
                    print(f"[TOOL USE] Jarvis executing modular hook: {function_name}({arguments})")
                    tool_output = registry.execute(function_name, arguments)
                    
                    if isinstance(tool_output, list):
                        tool_output = "\n".join(tool_output) if tool_output else "Empty directory state."
                    
                    messages.append({
                        'role': 'tool',
                        'content': str(tool_output),
                        'name': function_name
                    })
                
                print("[PROCESSING] Synthesizing downstream tool context values...")
                final_response = ollama.chat(model=self.model, messages=messages)
                return final_response['message']['content'].strip()
            
            return response['message']['content'].strip()
            
        except Exception as e:
            print(f"[ERROR] Modular brain architecture offline: {e}")
            return "I am currently disconnected from my cognitive framework, sir."