from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
     path('equipments/', include('backend.equipments.components.equipments.url')),
     path('employee/', include('backend.users.urls')),
     path('type-of-equipments/', include('backend.equipments.components.equipmentType.url')),
     path('reservation/', include('backend.equipments.components.reservation.url')),
]