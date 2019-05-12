from django.urls import path
from django.views.generic import TemplateView
from .view import ListEquipments, EquipmentUdView, EquipmentReadView, EquipmentCreateView

urlpatterns = [ 

    #Show whole Equipments
    # url = http://localhost:8000/api/manage/equipments/
    path('', ListEquipments.as_view()),

    # url = http://localhost:8000/api/manage/equipments/create
    path('create', EquipmentCreateView.as_view()),

    #Update or Delete specific Equipment
    # url = http://localhost:8000/api/manage/equipments/update-or-delete/1
    path('update-or-delete/<pk>', EquipmentUdView.as_view()),

    #Show a specific equipment
    # url = http://localhost:8000/api/manage/equipments/show/1
    path('show/<pk>', EquipmentReadView.as_view(), name="equipment-rud"),
]