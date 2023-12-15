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

