from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

# Create your tests here.


class SnackTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester",
            email="test@email.com",
            password="pass",
        )
        self.snack = Snack.objects.create(
            name="pickle", purchaser=self.user, description="so yummy"
        )

    def test_list_page_code(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_list_page_template(self):
        url = reverse("snack_list")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "snack_list.html")
        self.assertTemplateUsed(response, "base.html")

    def test_list_view(self):
        response = self.client.get(reverse("snack_list"))
        # self.assertEqual(response.status_code, 200)
        self.assertContains(response, "pickle")
