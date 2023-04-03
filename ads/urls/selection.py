from rest_framework import routers

from ads.views.selection import *

router = routers.SimpleRouter()
router.register('', SelectionViewSet)

urlpatterns = router.urls