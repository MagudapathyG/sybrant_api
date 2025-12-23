# profiles/serializers.py
from rest_framework import serializers
from .models import PersonalProfile

class PersonalProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalProfile
        fields = '__all__'
