from django.db.models import Q
from django.http import HttpResponse
from django.db import connection
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from ...models import Booked
from .serializer import BookedSerializer, ListBookedSerializer

##########################
# TODO : 
# - Create a class who show only Equipments who don't exist yet
##########################

#################################
# Create Update And Delete Only #
################################

class CsrfExempt(SessionAuthentication):
    def enforce_csrf(self, request):
        return 

class BookedAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BookedSerializer
    authentication_classes = (CsrfExempt, BasicAuthentication)
    queryset = Booked.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookedUdView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    authentication_classes = (CsrfExempt, BasicAuthentication)
    serializer_class = BookedSerializer

    def get_queryset(self):
        post = Booked.objects.all()
        return post

##################################################
# List Only  #
##################################################

class ListBooked(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ListBookedSerializer
    authentication_classes = (CsrfExempt, BasicAuthentication)
    queryset = Booked.objects.all()

#Reservation
class SpecificBooked(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = ListBookedSerializer
    authentication_classes = (CsrfExempt, BasicAuthentication)
    queryset = Booked.objects.all()