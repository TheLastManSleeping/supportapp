
from django.db import models

from django.utils import timezone


class Ticket(models.Model):
    State = [
        ('Unsolved', 'Unsolved'),
        ('Solved', 'Solved'),
        ('Frozen', 'Frozen'),
    ]
    state = models.CharField(
        max_length=15,
        choices=State,
        default='Unsolved',
    )
    title = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(editable=False, default=timezone.now)
    created_by = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    email = models.EmailField(default='')


class Message(models.Model):
    created = models.DateTimeField(editable=False, default=timezone.now)
    created_by = models.CharField(max_length=100, blank=True, default='')
    body = models.TextField(blank=True, default='')
    ticket = models.ForeignKey(Ticket, verbose_name="ticket", on_delete=models.CASCADE, related_name="messages")
