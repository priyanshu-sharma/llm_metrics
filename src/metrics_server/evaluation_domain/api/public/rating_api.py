from evaluation_domain.models import Rating

def create_rating(response_id, rating_type, metrics):
    rating = Rating.create(response_id, rating_type, metrics)
    return {
        'id': rating.id,
        'response': rating.response,
        'rating_type': rating.rating_type,
        'metrics': rating.metrics,
        'meta': rating.meta,
    }