from rest_framework import serializers
from ...models import EquipmentType 

class EquipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentType
        fields = ('__all__')
        read_only_fields = ['id']


class ListEquipmentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentType
        fields = ('__all__')
        read_only_fields = ['id']
        depth = 1