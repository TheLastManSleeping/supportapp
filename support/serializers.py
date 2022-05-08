from rest_framework import serializers

from support.models import Ticket, Message


class TicketList(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("id", "created", "created_by", "title", "state")


class MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("created", "created_by", "body")


class TicketDetailSerializer(serializers.ModelSerializer):
    messages = MessagesSerializer(many=True)

    class Meta:
        model = Ticket
        exclude = ("email",)


class TicketCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ("state",)


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("created_by", "body", "ticket")


class ChangeStateSerializer(serializers.ModelSerializer):
    state = serializers.CharField(max_length=255)

    class Meta:
        model = Ticket
        fields = ("state",)
