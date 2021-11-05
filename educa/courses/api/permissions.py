from rest_framework.permissions import BasePermission


class IsEnrolled(BasePermission):
    """
    Ограничение доступа к содержимому курсов для пользователей,
    не записанных на него.

    """

    def has_object_permission(self, request, view, obj):
        return obj.students.filter(id=request.user.id).exists()
