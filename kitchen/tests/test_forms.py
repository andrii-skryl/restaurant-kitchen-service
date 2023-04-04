from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.forms import CookCreationForm
from kitchen.models import DishType, Dish


class FormsTests(TestCase):
    def test_cook_creation_form_with_experience_first_last_name_is_valid(self):
        form_data = {
            "username": "test",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "Test First",
            "last_name": "Test Last",
            "years_of_experience": 10
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)


class SearchFormsTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="user12345"
        )
        self.client.force_login(self.user)

    def test_dish_type_search_form(self):
        search_request = "Soups"
        response = self.client.get(f"/dish-types/?name={search_request}")
        result_queryset = response.context["dish_type_list"]
        expected_queryset = DishType.objects.filter(
            name__icontains=search_request
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(result_queryset), list(expected_queryset))

    def test_cook_search_form(self):
        search_request = "john.smith"
        response = self.client.get(f"/cooks/?username={search_request}")
        result_queryset = response.context["cook_list"]
        expected_queryset = get_user_model().objects.filter(
            username__icontains=search_request
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(result_queryset), list(expected_queryset))

    def test_dish_search_form(self):
        search_request = "Borsch"
        response = self.client.get(f"/dishes/?name={search_request}")
        result_queryset = response.context["dish_list"]
        expected_queryset = Dish.objects.filter(name__icontains=search_request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(result_queryset), list(expected_queryset))
