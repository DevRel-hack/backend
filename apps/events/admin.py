from django.contrib import admin

from .models import Event, Participant


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "status", "title", "start_at", "is_internal", "form")
    empty_value_display = "-пусто-"


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("id", "event", "specialist", "role")
    empty_value_display = "-пусто-"
