from django.db.models import Q
from django.http import HttpResponse
from django.db import connection
from rest_framework import generics, mixins
from rest_framework.response import Response
from ...models import Booked
from .serializer import BookedSerializer, ListBookedSerializer

##########################
# TODO : 
# - Create a class who show only Equipments who don't exist yet
##########################

#################################
# Create Update And Delete Only #
################################

class BookedAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BookedSerializer
    queryset = Booked.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class BookedUdView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
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
    queryset = Booked.objects.all()

#Reservation
class SpecificBooked(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = ListBookedSerializer
    queryset = Booked.objects.all()