from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import *


# 쪽지
class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = ("pk", "calender", "nickname", "content", "created_at", "is_opened")

    

# 캘린더
class CalenderSerializer(serializers.ModelSerializer):
    letters = LetterSerializer(many=True, read_only=True)
    # owner = serializers.ReadOnlyField(source = 'user.username')
    name = serializers.SerializerMethodField(method_name="get_username")
    
    class Meta:
        model = Calender
        fields = ("pk", "owner", "name", "letters")
        read_only_fields = ("owner",)
    
    def get_username(self, obj):
        return obj.owner.username