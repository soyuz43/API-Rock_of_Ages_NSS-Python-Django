# File Path: API-Rock_of_Ages_NSS-Python-Django/rockapi/serializers.py

from rest_framework import serializers
from rockapi.models import Rock, Type
from django.contrib.auth.models import User  # ! Added import for User model

class RockTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for rock type"""

    class Meta:
        model = Type
        fields = ('label',)  # ! Include only the label field

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for user"""

    class Meta:
        model = User
        fields = ('first_name', 'last_name')  # ! Include first and last name fields

class RockSerializer(serializers.ModelSerializer):
    """JSON serializer for rock"""

    type = RockTypeSerializer(many=False)  # ! Use RockTypeSerializer for the type field
    user = UserSerializer(many=False)  # ! Use UserSerializer for the user field

    class Meta:
        model = Rock
        fields = ('id', 'name', 'weight', 'user', 'type')  # ! Updated fields to include 'user' and 'type'
