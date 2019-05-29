from django.urls import path
from django.views.generic import TemplateView
from .views import LocationAPIView, LocationRudView

urlpatterns = [
    #CR Equipment's type
    # url = http://localhost:8000/api/manage/location/
    path('', LocationAPIView.as_view()),
    
    # url = http://localhost:8000/api/manage/location/show/<pk>
    path('show/<pk>', LocationRudView.as_view()),

    # url = http://localhost:8000/api/manage/location/update-or-delete/<pk>
    path('update-or-delete/<pk>', LocationRudView.as_view()),
]