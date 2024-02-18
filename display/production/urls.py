from django.urls import path

from production.views import list_production

app_name = 'productions'


urlpatterns = [
    path('',list_production,name='list_production')
]





