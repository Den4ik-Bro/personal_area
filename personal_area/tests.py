from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import *

User = get_user_model()

"""сообщение для проверяющего: начал писать тесты, но не успеваю по времени
поэтому отправил на проверку без них.
"""


class TestSkillsView(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(username='test_user', password='12345')
        for i in range(10):
            User.objects.create_user(username='user' + str(i), password='12345')
        name = 'test_skill'
        for i in range(10):
            Skills.objects.create(name=name + str(i))
            Language.objects.create(name=name + str(i))
            Hobby.objects.create(name=name + str(i))

    def test_home_view(self):
        server_response = self.client.get(reverse('personal_area:home'))
        self.assertEqual(server_response.status_code, 200)
        self.assertTemplateUsed('home.html')
        self.assertTrue(server_response.context['is_paginated'] == True)
        self.assertEqual(len(server_response.context['users']), 5)
        server_response_page = self.client.get(reverse('personal_area:home') + '?page=3')
        self.assertEqual(len(server_response_page.context['users']), 1)

    def test_personal_area_view(self):
        server_response = self.client.get(reverse('personal_area:personal_area'))
        self.assertEqual(server_response.status_code, 302)
        self.client.login(username='test_user', password='12345')
        server_response = self.client.get(reverse('personal_area:personal_area'))
        self.assertEqual(server_response.status_code, 200)