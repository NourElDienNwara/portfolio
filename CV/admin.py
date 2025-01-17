from django.contrib import admin
from .models import *

# Register your models here.


class SkillsInline(admin.TabularInline):
    model = Skills
    extra = 1


class Admin_Sitting_Portfolio(admin.ModelAdmin):
    inlines = [SkillsInline]


class Admin_Sitting_Certificate(admin.ModelAdmin):
    list_display = ["title", "track", "date"]
    list_filter = ["track"]
    search_fields = ["title"]


admin.site.register(Portfolio, Admin_Sitting_Portfolio)
admin.site.register(Certificate, Admin_Sitting_Certificate)
