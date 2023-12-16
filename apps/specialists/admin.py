from django.contrib import admin


from .models import Specialist


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone",
        "email",
        "is_colleague",
    )
    empty_value_display = "-пусто-"
    search_fields = ("email", "city", "grade", "tools", "job")
