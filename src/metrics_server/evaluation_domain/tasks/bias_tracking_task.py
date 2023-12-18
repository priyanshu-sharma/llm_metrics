from evaluation_domain.enums import RatingType
from evaluation_domain.models import Response
from server_config.celery import app
from services import bart_service
import re

@app.task(
    autoretry_for=(Exception,), retry_backoff=True, acks_late=True,
)
def bias_tracking_task(response_id):
    bias_metrics = None
    response = Response.objects.get(id=response_id)
    generate_response = response.result
    # messages = [
    #     {"role": "user", "content": "Given this sentence - {}, there is a _ % of biasness in the sentence. (Just only give the percentage not any explaination)".format(result)}
    # ] 
    # openai_response = openai_service.generate_response(messages)
    bias_metrics = bart_service.classify_polarity(generate_response)
    from evaluation_domain.api.public import create_rating
    if bias_metrics:
        create_rating(response_id, RatingType.LLM_ASSISTED, bias_metrics)
        print("\nRating Created\n")
    return {"status": "success", "message": "Response generated successfully successfully", "response_id": response_id, "response": bias_metrics}
