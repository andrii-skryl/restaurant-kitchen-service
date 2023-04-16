from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="admin12345"
        )
        self.client.force_login(self.admin_user)
        self.cook = get_user_model().objects.create_user(
            username="cook",
            password="cook12345",
            years_of_experience=10
        )

    def test_cook_years_f_experience_listed(self):
        url = reverse("admin:kitchen_cook_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.cook.years_of_experience)

    def test_cook_detailed_years_of_experience_listed(self):
        url = reverse("admin:kitchen_cook_change", args=[self.cook.id])
        response = self.client.get(url)

        self.assertContains(response, self.cook.years_of_experience)

    def test_cook_additional_info_years_of_experience_listed(self):
        url = reverse("admin:kitchen_cook_add")
        response = self.client.get(url)

        self.assertContains(response, "first_name")
        self.assertContains(response, "last_name")
        self.assertContains(response, "years_of_experience")
