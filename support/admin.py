from django.contrib import admin

from support.models import Ticket, Message


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("state", "title", "created", "created_by", "id", "email")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ( "body", "created", "created_by", "ticket", "id")