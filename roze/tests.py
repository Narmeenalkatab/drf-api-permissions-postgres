from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Roze
# Create your tests here.
class RozeTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass"
        )
        testuser1.save()
        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass2"
        )
        testuser2.save()



        test_roze = Roze.objects.create(
            name="rake",
            owner=testuser1,
            desc="Better for collecting leaves than a shovel.",
        )
        test_roze.save()

    def setUp(self) -> None:
         self.client.login(username="testuser1", password="pass")


    def test_roze_model(self):
        roze = Roze.objects.get(id=1)
        actual_owner = str(roze.owner)
        actual_name = str(roze.name)
        actual_desc = str(roze.desc)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "rake")
        self.assertEqual(
            actual_desc, "Better for collecting leaves than a shovel."
        )

    def test_get_roze_list(self):
        url = reverse("roze_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        rozes = response.data
        self.assertEqual(len(rozes), 1)
        self.assertEqual(roze[0]["name"], "rake")


    def test_auth_required(self):
        self.client.logout()
        url = reverse("roze_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_only_owner_can_delete_roze(self):
        self.client.logout()
        self.client.login(username="testuser2", password="pass2")
        url = reverse("rozes_detail",args=[1])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
