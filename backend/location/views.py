from django.db.models import Q
from django.http import HttpResponse
from django.db import connection
from rest_framework import generics, mixins
from rest_framework.response import Response
from .models import Location
from .serializer import LocationSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class CsrfExempt(SessionAuthentication):
    def enforce_csrf(self, request):
        return 

class LocationAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = LocationSerializer
    queryset = Location.objects.all()
    authentication_classes = (CsrfExempt, BasicAuthentication)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class LocationRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = LocationSerializer
    authentication_classes = (CsrfExempt, BasicAuthentication)

    def get_queryset(self):
        post = Location.objects.all()
        return post