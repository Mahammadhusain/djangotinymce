from django.contrib import admin
from .models import DemoModel
# Register your models here.

@admin.register(DemoModel)
class DemoModelAdmin(admin.ModelAdmin):
    list_display = ("body","id")[::-1]


