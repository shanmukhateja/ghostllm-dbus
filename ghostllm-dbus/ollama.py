from ollama import generate
from ollama import GenerateResponse

from .constants import OLLAMA_MODEL_NAME, OLLAMA_SYSTEM_PROMPT

class OllamaController():

    def chat(self, input_str: str) -> str:
        response: GenerateResponse = generate(
            model=OLLAMA_MODEL_NAME,
            system=OLLAMA_SYSTEM_PROMPT,
            stream=False,
            prompt= f'rewrite "{input_str}"'
        )

        return response.response