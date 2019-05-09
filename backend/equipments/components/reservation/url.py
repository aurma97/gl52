from django.urls import path
from django.views.generic import TemplateView
from .view import *

urlpatterns = [
    #CRUD book
    # url = http://localhost:8000/api/manage/reservation/
    path('', ListBooked.as_view()),

    # url = http://localhost:8000/api/manage/reservation/create
    path('create', BookedAPIView.as_view()),

    # url = http://localhost:8000/api/manage/reservation/show<pk>
    path('show/<pk>', SpecificBooked.as_view()),

    # url = http://localhost:8000/api/manage/reservation/update-or-delete/<pk>
    path('update-or-delete/<pk>', BookedUdView.as_view()),
]