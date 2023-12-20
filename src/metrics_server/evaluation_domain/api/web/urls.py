from rest_framework.routers import DefaultRouter
from django.urls import re_path, include
from evaluation_domain.api.web.viewsets import UploadViewset, RatingViewset

router = DefaultRouter()
router.register(
    r"", UploadViewset, basename="upload",
)

router.register(
    r"rating", RatingViewset, basename="rating",
)

urlpatterns = [
    re_path("", include(router.urls)),
]
