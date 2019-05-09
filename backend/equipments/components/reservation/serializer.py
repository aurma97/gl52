from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from ...models import Booked


#For everything without join (Create, Update, Delete)

class BookedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booked
        fields =  ('__all__')
        read_only_fields = ['id']

    def validate_status(self, value):
        
            if self.instance:
                qs = Booked.objects.filter(status__iexact=value).filter(pk=self.instance.pk)
                
                #qs =  qs.exclude(pk=self.instance.pk)
            
                if qs.exists():
                    raise serializers.ValidationError("Le statut que vous essayé d'appliqué est déjà utilisé pour ce même équipement")
            return value
    

#For reading only with join (List)

class ListBookedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booked
        fields = ('__all__')
        read_only_fields = ['id']
        depth = 1
        # validators = [
        #     UniqueValidator(
        #         querySet = Booked.objects.all(),
        #         fields=('equipment_id')
        #         )
        # ]