from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from hikes.models import Hiker, DifficultyLevel, Region, Expedition


@admin.register(Hiker)
class HikerAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("fitness_level", "has_tent")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("fitness_level", "has_tent")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "fitness_level",
                    "has_tent",
                )
            },
        ),
    )


admin.site.register(DifficultyLevel)
admin.site.register(Region)
admin.site.register(Expedition)
