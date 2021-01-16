from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = 'You must be the owner of this object.'

    def has_object_permission(self, request, view, obj):
        return request.user == obj.user


class IsOwnerOrReadOnly(permissions.BasePermission):
    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS', 'POST')
    message = 'You must be the owner of this object.'

    def has_permission(self, request, view):
        return request.method in self.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.method in self.SAFE_METHODS:
            return True
        return request.user == obj.user
