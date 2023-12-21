from evaluation_domain.enums import RatingType
from evaluation_domain.models import Response
from server_config.celery import app
from services import openai_service
import re

@app.task(
    autoretry_for=(Exception,), retry_backoff=True, acks_late=True,
)
def correctness_tracking_task(response_id):
    response = Response.objects.get(id=response_id)
    result = response.result
    messages = [
        {"role": "user", "content": "Given this sentence - {}, there is a _ % of correctness in the sentence. (Just only give the percentage not any explaination)".format(result)}
    ] 
    openai_response = openai_service.generate_response(messages)
    if len(openai_response) < 4:
        correctness_precentage = openai_response
    else:
        correctness_precentage = re.findall('\d*%', openai_response)
    from evaluation_domain.api.public import create_rating
    if correctness_precentage:
        create_rating(response_id, RatingType.LLM_ASSISTED, {'correctness_precentage': correctness_precentage[0]})
        print("\nRating Created\n")
    return {"status": "success", "message": "Response generated successfully successfully", "response_id": response_id, "response": openai_response}
