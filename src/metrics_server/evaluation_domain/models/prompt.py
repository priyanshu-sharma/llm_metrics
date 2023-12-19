import uuid
from django.db import models
from extensions.models import AutoTimestampedModel, UserTrackingModel
from evaluation_domain.enums import LlmModels, PromptStatus
from django.db.models.signals import post_save

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
        indexes = [
            models.Index(fields=['run_id']),
        ]

    @staticmethod
    def create(prompt_list):
        """
        Get or create a Prompt.
        """
        try:
            Prompt.objects.bulk_create(prompt_list)
            for prompt in prompt_list:
                post_save.send(Prompt, instance=prompt, created=True)
        except Exception as e:
            raise e
    
def evaluate_prompt(sender, instance, created, **kwargs):
    from evaluation_domain.tasks import generate_response_task
    if created:
        generate_response_task.delay(instance.id)

post_save.connect(evaluate_prompt, sender=Prompt)