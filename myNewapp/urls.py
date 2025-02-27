from django.urls import path
from . import views

urlpatterns = [
    path('',views.modelformData,name = 'modelformData'),
]