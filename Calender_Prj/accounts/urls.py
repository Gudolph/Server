from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # accounts/password/change/
    # accounts/password/reset/
    # accounts/password/reset/confirm/
    # accounts/login/  -> 로그인
    # accounts/logout/
    # accounts/user/
    # accounts/token/verify/
    # accounts/token/refresh/
    # /accounts/registration/ -> 회원가입
    # 위의 url들 사용 가능
    path('', include('dj_rest_auth.urls')), 
    # 회원가입
    path("registration/", include('dj_rest_auth.registration.urls')),
    # 회원가입 기능 제공
    path('', include('allauth.urls')),
]