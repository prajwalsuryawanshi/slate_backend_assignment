from rest_framework import permissions

class CanAccessStudentAchievements(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        student_id = view.kwargs.get('student_id')

        if user.role == 'SCHOOL':
            return True
        elif user.role == 'PARENT' and user.linked_student_id == int(student_id):
            return True
        elif user.role == 'STUDENT' and user.id == int(student_id):
            return True
        return False


class CanManageStudentAchievements(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'SCHOOL'