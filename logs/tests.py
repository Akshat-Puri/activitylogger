from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from .models import UserActivityLog
from rest_framework import status

class UserActivityLogTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpass')

    def test_create_log(self):
        response = self.client.post('/activity-log/', {
            "action": "LOGIN",
            "metadata": {"ip": "127.0.0.1"}
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_logs(self):
        UserActivityLog.objects.create(user=self.user, action='LOGIN')
        response = self.client.get(f'/activity-log/user/{self.user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_status(self):
        log = UserActivityLog.objects.create(user=self.user, action='UPLOAD')
        response = self.client.patch(f'/activity-log/{log.id}/status/', {'status': 'DONE'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'DONE')
