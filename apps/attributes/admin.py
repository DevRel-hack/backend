from django.contrib import admin

from .models import City, Tool, Job, Grade, Tag, EventStatus, Role


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    empty_value_display = "-пусто-"
    search_fields = ("title",)


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    empty_value_display = "-пусто-"
    search_fields = ("title",)


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    empty_value_display = "-пусто-"
    search_fields = ("title",)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    empty_value_display = "-пусто-"
    search_fields = ("title",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    empty_value_display = "-пусто-"
    search_fields = ("title",)


@admin.register(EventStatus)
class EventStatusAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    empty_value_display = "-пусто-"
    search_fields = ("title",)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    empty_value_display = "-пусто-"
    search_fields = ("title",)
