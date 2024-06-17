# ! File Path: API-Rock_of_Ages_NSS-Python-Django/rockapi/serializers.py

from rest_framework import serializers
from rockapi.models import Rock, Type
from django.contrib.auth.models import User

class RockTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for rock type"""

    class Meta:
        model = Type
        fields = ('label',)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for user"""

    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class RockSerializer(serializers.ModelSerializer):
    """JSON serializer for rocks"""
    
    type = RockTypeSerializer(many=False)  # ! Include type serializer
    user = UserSerializer(many=False)  # ! Include user serializer

    class Meta:
        model = Rock
        fields = ('id', 'name', 'weight', 'user', 'type')  # ! Updated fields
