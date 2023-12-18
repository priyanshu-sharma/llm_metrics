import uuid
from django.db import models
from extensions.models import AutoTimestampedModel, UserTrackingModel
from evaluation_domain.enums import LlmModels, PromptStatus, PromptType
from django.db.models.signals import post_save

class Prompt(AutoTimestampedModel, UserTrackingModel):
    """
    Prompt model.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    run_id = models.UUIDField(default=uuid.uuid4, editable=False)
    sentence = models.TextField()
    llm_models = models.TextField(choices=LlmModels.choices(), default=LlmModels.CHAT_GPT)
    prompt_type = models.TextField(choices=PromptType.choices(), default=PromptType.QA)
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
    def get_or_create(run_id, sentence, llm_models, prompt_type):
        """
        Get or create a Images.
        """
        try:
            prompt = Prompt.objects.get(sentence=sentence, llm_models=llm_models, prompt_type=prompt_type, active=True)
        except Prompt.DoesNotExist:
            prompt = Prompt.objects.create(run_id=run_id, sentence=sentence, llm_models=llm_models, prompt_type=prompt_type, meta={}, active=True)
            prompt.save()
        return prompt
    
def evaluate_prompt(sender, instance, created, **kwargs):
    if created:
        print("Run ID - {}".format(instance.sentence))

post_save.connect(evaluate_prompt, sender=Prompt)