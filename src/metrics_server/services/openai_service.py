from openai import OpenAI
from server_config import OPENAI_KEY
from evaluation_domain.enums import LlmModels

class OpenAIService():
    def __init__(self):
        self.openai = OpenAI(api_key=OPENAI_KEY)
    
    def generate_response(self, messages):
        response = self.openai.chat.completions.create(model='gpt-3.5-turbo', messages=messages)
        return response.choices[0].message.content

    
