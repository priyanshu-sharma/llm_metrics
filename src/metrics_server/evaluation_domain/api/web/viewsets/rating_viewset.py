from rest_framework import viewsets, mixins
from evaluation_domain.models import Rating
from evaluation_domain.api.web.serializers import RatingSerializer
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from evaluation_domain.api.web.pagination import StandardPagination

class RatingViewset(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Rating.objects.filter(response__active=True, response__prompt__active=True).order_by('-install_ts')
    serializer_class = RatingSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    ordering_fields = ('install_ts',)
    ordering = ('install_ts',)
    pagination_class = StandardPagination