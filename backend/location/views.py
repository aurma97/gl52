from django.db.models import Q
from django.http import HttpResponse
from django.db import connection
from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import Location
from .serializer import LocationSerializer

class LocationAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class LocationRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = LocationSerializer

    def get_queryset(self):
        post = Location.objects.all()
        return post