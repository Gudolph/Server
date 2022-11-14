from rest_framework import serializers
from django.contrib import auth
from dj_rest_auth.registration.serializers import RegisterSerializer

User = auth.get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # fields = ['id', 'username','email', 'password']
        
class CustomRegisterSerializer(RegisterSerializer):
    username = serializers.CharField()
    # first_name = serializers.CharField()
    # gender = serializers.ChoiceField(choices=User.GenderChoices)
    # role = serializers.CㄴㄷhoiceField(choices=User.RoleChoices)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['username'] = self.validated_data.get('username', '')
        # data['first_name'] = self.validated_data.get('first_name', '')
        # data['gender'] = self.validated_data.get('gender', '')
        # data['role'] = self.validated_data.get('role', '')

        return data