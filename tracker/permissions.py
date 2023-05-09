from rest_framework.permissions import BasePermission


class UserPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user == view.get_object().user:
            return True
        return False
