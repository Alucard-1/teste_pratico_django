from django.urls import path
from django.http import HttpResponse
from production.views import list_production, button_1, change_status_production_to_started, button_2, change_status_production_started
from. import views


app_name = 'productions'






urlpatterns = [
    path('',list_production,name='list_production'),
    path('123/', button_1, name = 'button_1'),
    path('change-to-started/',change_status_production_to_started, name='change-to-started'),
    path('iniciados/', button_2, name='button_2'),
    path('change-started/',change_status_production_started, name='change-started'),
    
]








