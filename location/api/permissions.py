from rest_framework import permissions


class OnlyStudents(permissions.BasePermission):
    message = 'Only students are allowed.'

    def has_permission(self, request, view):
        if str(request.user) == 'AnonymousUser':
            return False
        return request.user.is_student


class OnlyTeachers(permissions.BasePermission):
    message = 'Only teachers are allowed.'

    def has_permission(self, request, view):
        if str(request.user) == 'AnonymousUser':
            return False
        return request.user.is_teacher


class OnlyTeachersOrStudents(permissions.BasePermission):
    message = 'Only teachers or students are allowed.'

    def has_permission(self, request, view):
        if str(request.user) == 'AnonymousUser':
            return False
        return request.user.is_teacher or request.user.is_student

class OnlyAdmin(permissions.BasePermission):
    message = 'Only Admin are allowed.'

    def has_permission(self, request, view):
        if str(request.user) == 'AnonymousUser':
            return False
        return request.user.is_institution_adm
