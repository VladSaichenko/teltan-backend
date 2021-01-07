from rest_framework import permissions


class IsUsersProfile(permissions.BasePermission):
    message = 'It must be your account.'

    def has_object_permission(self, request, view, obj):
        return request.user == obj
