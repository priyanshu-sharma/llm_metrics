from evaluation_domain.enums import PromptStatus
from evaluation_domain.models import Prompt
from server_config.celery import app
from services import openai_service

@app.task(
    autoretry_for=(Exception,), retry_backoff=True, acks_late=True,
)
def generate_response_task(prompt_id):
    prompt = Prompt.objects.get(id=prompt_id)
    messages = [
        {"role": "user", "content": prompt.sentence}
    ] 
    response = openai_service.generate_response(messages)
    prompt.prompt_status = PromptStatus.COMPLETED
    prompt.save()
    from evaluation_domain.api.public import create_response
    create_response(prompt_id, response)
    return {"status": "success", "message": "Response generated successfully successfully", "prompt_id": prompt_id, "response": response}
