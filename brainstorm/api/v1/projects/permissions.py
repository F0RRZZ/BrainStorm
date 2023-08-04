import rest_framework.permissions


class IsOwnerOrReadOnly(rest_framework.permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated():
            return False
        if request.method in rest_framework.permissions.SAFE_METHODS:
            return True
        return obj.author == request.user or request.user.is_staff
