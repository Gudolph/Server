from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from datetime import datetime

# from .permissions import *
from .serializers import *
from .models import *
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated,IsAuthenticatedOrReadOnly
# 캘린더
class CalenderViewSet(viewsets.ModelViewSet):
    queryset = Calender.objects.all()
    serializer_class = CalenderSerializer
    
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def list(self, request):
        return super().list(request)
    
    # def retrieve(self, request, pk=None):
    #     pass  

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
    def get_queryset(self):
        user = self.request.user
        
        # 더미 데이터
        # letter = get_object_or_404(Letter, pk=2)
        
        # self.letters.append(letter)
        
        # user = self.request.user
        # calender = self.request.user.calender
        
        # open = datetime(2022, 12, 1)
        # now = datetime.now()
        
        # # 24개 미만의 편지가 들어왔을 때 24개까지 sample data 넣어줌
        # if open == now:
        #     if (calender.num < 24):
        #         while(calender.num == 24):
        #             i = 2
                    
        #             # 편지 객체 넣어주기
        #             letter = get_object_or_404(Letter, pk=i)
        #             self.letters.append(letter)
                    
        #             i += 1
        #             calender.num += 1
            
        return Calender.objects.filter(owner=user)

# 쪽지
class LetterViewSet(viewsets.ModelViewSet):
    queryset = Letter.objects.all()
    serializer_class = LetterSerializer
    
    # def perform_create(self, serializer):
    #     calender = self.request.calender
    #     calender.num += 1
    
    def partial_update(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.serialize(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)

        