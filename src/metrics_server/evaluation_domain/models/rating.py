import uuid
from django.db import models
from extensions.models import AutoTimestampedModel, UserTrackingModel
from evaluation_domain.enums import RatingType
from evaluation_domain.models import Response


class Rating(AutoTimestampedModel, UserTrackingModel):
    """
    Rating model.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    response = models.ForeignKey(Response, on_delete=models.CASCADE)
    rating_type = models.TextField(choices=RatingType.choices(), default=RatingType.LLM_ASSISTED)
    metrics = models.JSONField(default=dict)
    meta = models.JSONField(default=dict)

    class Meta:
        db_table = 'rating'
        app_label = 'evaluation_domain'

    @staticmethod
    def create(response_id, rating_type, metrics):
        """
        Get or create a Rating.
        """
        try:
            rating = Rating.objects.create(response_id=response_id, rating_type=rating_type, metrics=metrics, meta={})
            rating.save()
            return rating
        except Exception as e:
            raise NotImplementedError