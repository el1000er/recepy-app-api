""" Test for Django admin modifications. """
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSitetest(TestCase):
    """ Tests for Django admin. """

    def setUp(self):
        """ Create user and django test client. """
        self.client = Client()
        self.admin_user = get_user_model().object.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )
        """ force_login allows us to foce the authentication to
        the creted user """
        self.client.force_login(self.admin_user)
        """ Create a user in  the db for testing """
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass123',
            name='Test user'
            )

    def test_user_list(self):
        """ Unit test that users are listed on page. """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
