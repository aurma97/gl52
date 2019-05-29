from rest_framework import serializers
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
        read_only_fields = ['id']

# class ListEquipmentsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('__all__')
#         read_only_fields = ['id']
#         depth = 1