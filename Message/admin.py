from django.contrib import admin
from .models import *

# Register your models here.


class Admin_Sitting_Message(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "active"]
    list_filter = ["active"]
    search_fields = ["name", "email"]


admin.site.register(Messages, Admin_Sitting_Message)
