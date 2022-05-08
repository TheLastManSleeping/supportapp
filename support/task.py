from django.core.mail import send_mail
from supportapp.celery import app


@app.task
def send(email):
    send_mail(
        'Ticket',
        'One of your tickets just`ve got it state changed!',
        '',
        [email],
        fail_silently=False,
    )
