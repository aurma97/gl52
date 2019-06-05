from django.db.models import Q
from django.http import HttpResponse
from django.db import connection
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from ...models import EquipmentType
from .serializer import EquipmentTypeSerializer, ListEquipmentTypeSerializer

class CsrfExempt(SessionAuthentication):
    def enforce_csrf(self, request):
        return 

class EquipmentTypeAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = EquipmentTypeSerializer
    queryset = EquipmentType.objects.all()
    authentication_classes = (CsrfExempt, BasicAuthentication)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class EquipmentTypeRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EquipmentTypeSerializer
    authentication_classes = (CsrfExempt, BasicAuthentication)

    def get_queryset(self):
        post = EquipmentType.objects.all()
        return post