from django.http import HttpResponse
from django.db import connection
from rest_framework import generics, mixins
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializer import EmployeeSerializer

class EmployeeAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = EmployeeSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class EmployeeRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        post = User.objects.all()
        return post