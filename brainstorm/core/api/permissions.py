import rest_framework.permissions


class IsAdminOrReadOnly(rest_framework.permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated():
            return False
        if request.method in rest_framework.permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
