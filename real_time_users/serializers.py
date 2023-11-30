from rest_framework import serializers
from .models import UserActions


class UserActionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserActions
        fields = '__all__'

