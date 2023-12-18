from services.openai_service import OpenAIService
from services.bart_service import BartService

openai_service = OpenAIService()
bart_service = BartService()

__all__ = ('openai_service', 'bart_service')