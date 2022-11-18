from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework.routers import DefaultRouter

# http://127.0.0.1:8000/calenderMain/

router = DefaultRouter()
router.register(r'my-calender', views.ShowLetterViewSet, basename="my-calender")
urlpatterns = [
    # http://127.0.0.1:8000/accounts/registration -> 회원가입
    # http://127.0.0.1:8000/accounts/login -> 로그인
    # http://127.0.0.1:8000/accounts/user -> 현재 유저가 누구인지 확인
    # http://127.0.0.1:8000/accounts/logout -> 로그아웃
    
    # http://127.0.0.1:8000/calenderMain/my-calender -> 작성한 쪽지 보기, 쪽지 생성 : 임시로 만든거라 수정 예정
    path('', include(router.urls)),
    # path("", views.home, name='home'),
]