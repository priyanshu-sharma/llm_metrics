from openai import OpenAI
from server_config import OPENAI_KEY
from evaluation_domain.enums import LlmModels

class OpenAIService():
    def __init__(self):
        self.openai = OpenAI(api_key=OPENAI_KEY)
        self.model_map = {
            LlmModels.CHAT_GPT: 'gpt-3.5-turbo'
        }
    
    def generate_response(self, model, messages):
        openai_model = self.model_map[model]
        response = self.openai.chat.completions.create(model=openai_model, messages=messages)
        return response.choices[0].message.content

    
