from rest_framework import viewsets, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from support.models import Ticket
from support.serializers import MessageCreateSerializer, TicketDetailSerializer, TicketCreateSerializer, \
    ChangeStateSerializer
from .task import send


class TicketViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def partial_update(self, request, pk=None, **kwargs):
        if not request.user.is_staff:
            return Response(status=403)
        queryset = Ticket.objects.all()
        ticket = get_object_or_404(queryset, pk=pk)
        serializer = ChangeStateSerializer(ticket, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            send(ticket.email)
            return Response(status=202)

        else:
            return Response(status=403)

    def create(self, request, **kwargs):
        ticket = TicketCreateSerializer(data=request.data)
        if ticket.is_valid():
            ticket.save()
        return Response(status=201)

    def list(self, request, **kwargs):
        if request.user.is_staff:
            ticket = Ticket.objects.all()
        else:
            ticket = Ticket.objects.filter(created_by=request.user.username)
        serializer = TicketDetailSerializer(ticket, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = Ticket.objects.all()
        ticket = get_object_or_404(queryset, pk=pk)
        serializer = TicketDetailSerializer(ticket)
        return Response(serializer.data)


class MessageViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        message = MessageCreateSerializer(data=request.data)
        if message.is_valid():
            message.save()
        else:
            return Response(status=403)
        return Response(status=201)
