import rest_framework.routers

import api.v1.projects.views

router = rest_framework.routers.DefaultRouter()
router.register(
    r'projectlist',
    api.v1.projects.views.ProjectViewSet,
    basename='projectlist',
)
