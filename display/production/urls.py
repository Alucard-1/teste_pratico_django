from django.urls import path
from django.http import HttpResponse
from production.views import list_production, production_started, change_status_production_to_started, concluded, change_status_production_concluded



app_name = 'productions'






urlpatterns = [
    path('',list_production,name='list_production'),
    path('started/', production_started, name = 'production_started'),
    path('change-to-started/',change_status_production_to_started, name='change-to-started'),
    path('concluded/', concluded, name='concluded'),
    path('change-started/',change_status_production_concluded, name='change-started'),
    
]








