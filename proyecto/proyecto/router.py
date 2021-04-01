from proyecto1.viewsets import EnterpriseViewset,CodeViewset

from rest_framework import routers

router = routers.DefaultRouter()

router.register('enterprise-c',EnterpriseViewset, basename="enterprise-c")
router.register('code',CodeViewset,basename="code")

# localhost:p/api