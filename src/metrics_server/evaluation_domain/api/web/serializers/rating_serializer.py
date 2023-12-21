from rest_framework import serializers
from evaluation_domain.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    response__prompt__id = serializers.UUIDField(source='response.prompt.id')
    response__prompt__run_id = serializers.UUIDField(source='response.prompt.run_id')
    response__prompt__sentence = serializers.CharField(source='response.prompt.sentence')
    response__prompt__llm_models = serializers.CharField(source='response.prompt.llm_models')
    response__prompt__prompt_status = serializers.CharField(source='response.prompt.prompt_status')
    response__prompt__meta = serializers.JSONField(source='response.prompt.meta')
    response__id = serializers.UUIDField(source='response.id')
    response__result = serializers.CharField(source='response.result')
    response__overall_metrics = serializers.JSONField(source='response.overall_metrics')
    response__meta = serializers.JSONField(source='response.meta')
    class Meta:
        model = Rating
        fields = (
            'response__prompt__id',
            'response__prompt__run_id',
            'response__prompt__sentence',
            'response__prompt__llm_models',
            'response__prompt__prompt_status',
            'response__prompt__meta',
            'response__id',
            'response__result',
            'response__overall_metrics',
            'response__meta',
            'id',
            'rating_type',
            'metrics',
            'meta',
        )
