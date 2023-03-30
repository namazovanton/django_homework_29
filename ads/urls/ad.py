from rest_framework import routers

from ads.views.ad import *

router = routers.SimpleRouter()
router.register('', AdViewSet)

urlpatterns = router.urls

