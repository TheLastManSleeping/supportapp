from django.core.mail import send_mail
from django_filters import rest_framework as filters

from support.models import Ticket


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class TicketFilter(filters.FilterSet):
    State = [
        ('Unsolved', 'Unsolved'),
        ('Solved', 'Solved'),
        ('Frozen', 'Frozen'),
    ]
    state = filters.ChoiceFilter(choices=State)
    title = CharFilterInFilter(field_name='title', lookup_expr='in')

    class Meta:
        model = Ticket
        fields = ["state", "title"]
