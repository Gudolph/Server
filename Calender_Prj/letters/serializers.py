from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import *


# 쪽지
class LetterSerializer(serializers.ModelSerializer):
    # receiver = serializers.ReadOnlyField(source='calender.name')
    class Meta:
        model = Letter
        fields = ("pk", "calender", "nickname", "content", "created_at")
        

# 캘린더
class CalenderSerializer(serializers.ModelSerializer):
    letters = LetterSerializer(many=True, read_only=True)
    owner = serializers.ReadOnlyField(source = 'user.username')
    
    class Meta:
        model = Calender
        fields = ("pk", "owner", "name", "letters")