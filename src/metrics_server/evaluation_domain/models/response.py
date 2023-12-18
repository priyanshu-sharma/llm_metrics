import uuid
from django.db import models
from extensions.models import AutoTimestampedModel, UserTrackingModel
from evaluation_domain.models import Prompt
from django.db.models.signals import post_save

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

def evaluate_response(sender, instance, created, **kwargs):
    from evaluation_domain.enums import TYPE_PROMPT_MAP
    from evaluation_domain.tasks import bias_tracking_task, correctness_tracking_task
    if created:
        prompt_type = instance.prompt.prompt_type
        print("Run ID - {}".format(prompt_type))
        possible_metrics = TYPE_PROMPT_MAP[prompt_type]['metrics']
        if 'bias' in possible_metrics:
            bias_tracking_task.delay(instance.id)
        if 'correctness' in possible_metrics:
            correctness_tracking_task.delay(instance.id)
        else:
            raise NotImplementedError


post_save.connect(evaluate_response, sender=Response)