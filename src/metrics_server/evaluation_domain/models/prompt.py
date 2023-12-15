import uuid
from django.db import models
from extensions.models import AutoTimestampedModel, UserTrackingModel
from evaluation_domain.enums import LlmModels, PromptStatus

class Prompt(AutoTimestampedModel, UserTrackingModel):
    """
    Prompt model.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    run_id = models.UUIDField(default=uuid.uuid4, editable=False)
    sentence = models.TextField()
    llm_models = models.TextField(choices=LlmModels.choices(), default=LlmModels.CHAT_GPT)
    prompt_status = models.TextField(choices=PromptStatus.choices(), default=PromptStatus.CREATED)
    meta = models.JSONField(default=dict)
    active = models.BooleanField()

    class Meta:
        db_table = 'prompt'
        app_label = 'evaluation_domain'
        unique_together = [('run_id', 'llm_models')]
        indexes = [
            models.Index(fields=['run_id']),
        ]
