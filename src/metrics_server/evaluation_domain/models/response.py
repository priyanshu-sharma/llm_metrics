import uuid
from django.db import models
from extensions.models import AutoTimestampedModel, UserTrackingModel
from evaluation_domain.models import Prompt


class Response(AutoTimestampedModel, UserTrackingModel):
    """
    Response model.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    prompt = models.ForeignKey(Prompt, on_delete=models.CASCADE)
    result = models.TextField()
    overall_metrics = models.JSONField(default=dict)
    meta = models.JSONField(default=dict)
    active = models.BooleanField()

    class Meta:
        db_table = 'response'
        app_label = 'evaluation_domain'

    @staticmethod
    def create(prompt_id, result):
        """
        Get or create a Response.
        """
        try:
            response = Response.objects.create(prompt_id=prompt_id, result=result, overall_metrics={}, meta={}, active=True)
            response.save()
            return response
        except Exception as e:
            raise NotImplementedError