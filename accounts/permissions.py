from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    message = "siz admin emassiz"

    def has_permission(self, request, view):
        return request.user and request.user.is_admin
    
class IsUser(BasePermission):
    message = "siz admin emassiz"

    def has_permission(self, request, view):
        return request.user and request.user.is_user
    

class IsManager(BasePermission):
    message = "siz admin emassiz"

    def has_permission(self, request, view):
        return request.user and request.user.is_manager
    