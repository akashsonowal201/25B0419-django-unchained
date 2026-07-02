from django.contrib import admin

# Register your models here.
from .models import Bounty

@admin.register(Bounty)
class BountyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "target_name",
        "reward",
        "status",
        "owner",
        "created_at",
    )

    list_filter = ("status", "owner")

    search_fields = (
        "target_name",
        "owner__username",
    )