from django.db.models import Q
from django.http import HttpResponse
from django.db import connection
from rest_framework import generics, mixins
from rest_framework.response import Response
from ...models import Equipments
from .serializer import EquipmentsSerializer, ListEquipmentsSerializer


#################################
# Create Update And Delete Only #
################################

#Add an equipment (Can also see an equipment but list is not detailed)
class EquipmentCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = EquipmentsSerializer
    queryset = Equipments.objects.all().select_related('location').select_related('type_id')

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


#Update and Delete and Equipement
class EquipmentUdView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EquipmentsSerializer
    pass

    def get_queryset(self):
        post = Equipments.objects.all()
        return post


##################################################
# List Only  #
##################################################

class ListEquipments(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ListEquipmentsSerializer
    queryset = Equipments.objects.all()

#Specific Equipement
class EquipmentReadView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = ListEquipmentsSerializer
    queryset = Equipments.objects.all()
