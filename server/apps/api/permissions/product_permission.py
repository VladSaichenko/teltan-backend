from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    message = 'You can not update these fields.'

    def has_object_permission(self, request, view, obj):
        if request.data
