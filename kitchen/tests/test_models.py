from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen.models import DishType, Dish


class ModelTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="test"
        )
        self.assertEqual(
            str(dish_type),
            dish_type.name
        )

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="test",
            password="test12345",
            first_name="Test First",
            last_name="Test Last"
        )

        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="test"
        )
        dish = Dish.objects.create(
            name="Test Dish",
            dish_type=dish_type
        )

        self.assertEqual(
            str(dish),
            f"{dish.name} (price: {dish.price}, type: {dish.dish_type.name})"
        )

    def test_create_cook_with_years_of_experience(self):
        username = "test"
        password = "test12345"
        years_of_experience = 10

        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience
        )

        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)
