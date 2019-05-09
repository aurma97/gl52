from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    # List all and Create
    # url = http://localhost:8000/api/manage/employee/
    path('', EmployeeAPIView.as_view()),

    # List specific and Update, Delete
    # url = http://localhost:8000/api/manage/employee/<pk>
    path('<pk>', EmployeeRudView.as_view()),

]