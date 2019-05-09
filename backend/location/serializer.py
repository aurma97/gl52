from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        field = [
            'id',
            'name',
        ]
        read_only_fields = ['id']