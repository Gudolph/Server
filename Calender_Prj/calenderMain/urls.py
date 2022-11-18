from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rest_framework.routers import DefaultRouter

# http://127.0.0.1:8000/calenderMain/

router = DefaultRouter()
router.register(r'my-calender', views.ShowLetterViewSet, basename="my-calender")
urlpatterns = [
    # http://127.0.0.1:8000/calenderMain/my-calender
    path('', include(router.urls)),
    # path("", views.home, name='home'),
]