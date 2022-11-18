from rest_framework import permissions


# 쪽지 보내기 - 아무나, 쪽지 읽기 - 캘린더 생성자만
class CustomCreateOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user.is_authenticated
        return True