from rest_framework.permissions import BasePermission, IsAuthenticated


class IsAuthenticatedOrPublicAvailable(IsAuthenticated):

    def has_permission(self, request, view):
        from .views import ListTweetView

        if isinstance(view, (ListTweetView, )):
            return True

        return request.user and request.user.is_authenticated


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
