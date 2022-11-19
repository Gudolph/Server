from django.shortcuts import render

from rest_framework import generics
from rest_framework import viewsets

# from .permissions import *
from .serializers import *
from .models import *

# 캘린더
class CalenderViewSet(viewsets.ModelViewSet):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        user = self.request.user
        return Calender.objects.filter(owner=user)

# 쪽지
class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    
