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
        # try:
        response = Response.objects.create(prompt_id=prompt_id, result=result, overall_metrics={}, meta={}, active=True)
        response.save()
        return response
        # except Exception as e:
        #     raise NotImplementedError

def evaluate_response(sender, instance, created, **kwargs):
    from evaluation_domain.tasks import bias_tracking_task, correctness_tracking_task
    if created:
        metrics = instance.prompt.meta['metrics']
        if 'bias' in metrics:
            bias_tracking_task.delay(instance.id)
        if 'correctness' in metrics:
            correctness_tracking_task.delay(instance.id)


post_save.connect(evaluate_response, sender=Response)