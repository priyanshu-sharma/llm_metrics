from evaluation_domain.models import Response

def create_response(prompt_id, result):
    response = Response.create(prompt_id, result)
    return {
        'id': response.id,
        'prompt_id': response.prompt_id,
        'result': response.result,
        'overall_metrics': response.overall_metrics,
        'meta': response.meta,
        'active': response.active 
    }