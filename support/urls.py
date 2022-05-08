from rest_framework import routers

from .views import TicketViewSet, MessageViewSet

router = routers.SimpleRouter()
router.register(r"ticket", TicketViewSet, basename='ticket'),
router.register(r"message", MessageViewSet, basename='message'),

urlpatterns = router.urls
