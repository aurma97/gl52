from django.urls import path
from django.views.generic import TemplateView
from .view import EquipmentTypeAPIView, EquipmentTypeRudView

urlpatterns = [
    #CR Equipment's type
    # url = http://localhost:8000/api/manage/type-of-equipments/
    path('', EquipmentTypeAPIView.as_view()),
    
    # url = http://localhost:8000/api/manage/type-of-equipments/show/<pk>
    path('show/<pk>', EquipmentTypeRudView.as_view()),

    # url = http://localhost:8000/api/manage/type-of-equipments/update-or-delete/<pk>
    path('update-or-delete/<pk>', EquipmentTypeRudView.as_view()),
]