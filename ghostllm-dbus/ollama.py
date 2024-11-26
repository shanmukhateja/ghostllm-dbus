from ollama import chat
from ollama import ChatResponse

class OllamaController():
    
    def chat(self, input_str: str) -> str:
        response: ChatResponse = chat(
            model='llama3.2',
            messages=[
                {
                    'role': 'user',
                    'content': f'Rewrite the input string "{input_str}". I only need single sentence. don\'t reply with anything else',
                },
            ]
        )

        return response.message.content