from rest_framework import serializers
from .models import Letter
from django.contrib.auth.models import User

class LetterSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Letter
        fields = ['id', 'user', 'username','is_public', 'created_at', 'title', 'body']
        read_only_fields = ['id', 'user', 'is_public', 'created_at']

    def create(self, validated_data):
        letter = Letter.objects.create(**validated_data)
        return letter
        