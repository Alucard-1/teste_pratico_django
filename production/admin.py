from django.contrib import admin
from production.models import Sb1010, Sd3010

# Register your models here.
@admin.register(Sd3010)
@admin.register(Sb1010)

class Sd3010Admin(admin.ModelAdmin):
    pass

class Sb1010Admin(admin.ModelAdmin):
    pass

