from rest_framework.permissions import BasePermission, IsAuthenticated


class IsAuthenticatedOrPublicAvailable(IsAuthenticated):

    def has_permission(self, request, view):
        from .views import ListPublicTweetsView

        if isinstance(view, (ListPublicTweetsView, )):
            return True

        return request.user and request.user.is_authenticated


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        from .views import CreateDeleteLikeView

        if isinstance(view, (CreateDeleteLikeView, )):
            return str(obj.author.id) == str(request.user)

        return obj.owner == request.user
