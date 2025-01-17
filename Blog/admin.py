from django.contrib import admin
from .models import *

# Register your models here.


class Admin_Sitting_Blog(admin.ModelAdmin):
    list_display = ["title", "about"]
    list_filter = ["about"]
    search_fields = ["title"]


admin.site.register(Blog, Admin_Sitting_Blog)
