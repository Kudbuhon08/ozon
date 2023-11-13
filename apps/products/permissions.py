from rest_framework.permissions import BasePermission

class ProductPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(obj.shop.user.pk == request.user.pk)