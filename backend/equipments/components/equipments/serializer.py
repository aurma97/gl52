from rest_framework import serializers
from ...models import Equipments


class EquipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipments
        fields = ('__all__')
        read_only_fields = ['id']

class ListEquipmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipments
        fields = ('__all__')
        read_only_fields = ['id']
        depth = 1