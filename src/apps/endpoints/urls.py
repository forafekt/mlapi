from django.conf.urls import include
from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.endpoints.views import StopABTestView, PredictView, ABTestViewSet, MLRequestViewSet, \
    MLAlgorithmStatusViewSet, MLAlgorithmViewSet, EndpointViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"endpoints", EndpointViewSet, basename="endpoints")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgorithms")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet, basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")
router.register(r"abtests", ABTestViewSet, basename="abtests")

urlpatterns = [
    re_path(r"^api/v1/", include(router.urls)),
    re_path(
        r"^api/v1/(?P<endpoint_name>.+)/predict$", PredictView.as_view(), name="predict"
    ),
    re_path(
        r"^api/v1/stop_ab_test/(?P<ab_test_id>.+)", StopABTestView.as_view(), name="stop_ab"
    ),
]