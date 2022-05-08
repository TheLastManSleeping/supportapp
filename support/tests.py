from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class TestTickets(APITestCase):

    def authenticate(self):
        self.client.post(reverse('user-list'), {'username': "bob342",
                                                'password': "q12wer32ty",
                                                'email': "email@gmail.com"})
        response = self.client.post(reverse('jwt-create'), {'username': "bob342",
                                                            'password': "q12wer32ty"})
        self.client.credentials(HTTP_AUTHORIZATION=f"JWT {response.data['access']}")

    def test_get_tickets_unauthorized(self):
        response = self.client.post(reverse('ticket-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_tickets_authorized(self):
        self.authenticate()
        response = self.client.get(reverse('ticket-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_ticket_authorized(self):
        self.authenticate()
        sample = {'title': 'test',
                  'body': 'test',
                  'created_by': 'test',
                  'email': 'test'}
        response = self.client.post(reverse('ticket-list'), sample)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


