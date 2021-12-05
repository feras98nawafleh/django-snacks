from django.contrib import admin
from .models import Snacks

# Register your models here.
@admin.register(Snacks)
class AdminWork(admin.ModelAdmin):
  list_displays = ['name']