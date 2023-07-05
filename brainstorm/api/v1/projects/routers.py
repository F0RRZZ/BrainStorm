import rest_framework.routers

import api.v1.projects.views


router = rest_framework.routers.SimpleRouter()
router.register(r'projectlist', api.v1.projects.views.ProjectViewSet)
