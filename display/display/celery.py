# pratica\display\display\celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Define o nome do projeto Django para o Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'display.settings')

# Cria uma instância do Celery
app = Celery('pratica')

# Carrega as configurações do Django para o Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover para encontrar tarefas em seus aplicativos Django
app.autodiscover_tasks()
