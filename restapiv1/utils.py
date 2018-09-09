from rest_framework import permissions
from .pagination import APIPagination
from .permissions import IsOwner


def override_view_attributes(ref):
    ref.permission_classes = (permissions.IsAuthenticated,
                              IsOwner)
    ref.pagination_class = APIPagination
