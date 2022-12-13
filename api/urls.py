from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, MailingViewSet, MessageViewSet

app_name = "api"

router_v1 = DefaultRouter()

router_v1.register("mailings", MailingViewSet)
router_v1.register("clients", ClientViewSet)
router_v1.register("messages", MessageViewSet)

urlpatterns = [
    path("v1/", include(router_v1.urls))
]
