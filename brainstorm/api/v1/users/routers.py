import rest_framework.routers

import api.v1.users.views

router = rest_framework.routers.SimpleRouter()
router.register(r'userlist', api.v1.users.views.UserViewSet)
