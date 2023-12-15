from rest_framework.routers import DefaultRouter
from django.urls import re_path, include
from evaluation_domain.api.web.viewsets import UploadViewset

router = DefaultRouter()
router.register(
    r"", UploadViewset, basename="upload",
)

urlpatterns = [
    re_path("", include(router.urls)),
]
