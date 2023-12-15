"""
URL configuration for metrics_server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include, re_path
from server_config import health_check_view
from rest_framework_swagger.views import get_swagger_view
from evaluation_domain.api.web import urls as evaluation_domain_urls


schema_view = get_swagger_view(title='Metrics Server API')

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path("^health_check$", health_check_view),
    re_path('^docs', schema_view),
    re_path("^api/evaluation_domain/v1/", include((evaluation_domain_urls, 'evaluation_domain'), namespace='v1_evaluation_domain')),

]
