# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function, division
from test_plus.test import TestCase

from users.tests.factories import UserFactory


class TestUser(TestCase):
    user_factory = UserFactory

    def setUp(self):
        self.user = self.make_user(username='testuser@example.com')

    def test__str__(self):
        self.assertEqual(
            self.user.__str__(),
            'testuser@example.com'
        )
