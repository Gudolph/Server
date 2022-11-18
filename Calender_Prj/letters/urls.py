from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('calender', CalenderViewSet, basename='calender')
router.register('letter', LetterViewSet, basename='letter')

urlpatterns = [
    path('', include(router.urls)),
]

