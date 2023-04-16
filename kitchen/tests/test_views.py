from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from kitchen.models import DishType, Dish

DISH_TYPES_URL = reverse("kitchen:dish-type-list")
COOKS_URL = reverse("kitchen:cook-list")
DISHES_URL = reverse("kitchen:dish-list")


class PublicDishTypesTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        response = self.client.get(DISH_TYPES_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateDishTypesTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="user12345"
        )
        self.client.force_login(self.user)

    def test_retrieve_dish_types(self):
        DishType.objects.create(name="Desserts")

        response = self.client.get(DISH_TYPES_URL)
        dish_types = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_type_list"]),
            list(dish_types)
        )
        self.assertTemplateUsed(response, "kitchen/dish_type_list.html")


class PublicCookTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        response = self.client.get(COOKS_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateCooksTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="user12345"
        )
        self.client.force_login(self.user)

    def test_retrieve_cooks(self):
        get_user_model().objects.create_user(
            username="user",
            password="user12345",
            years_of_experience=10
        )

        response = self.client.get(COOKS_URL)
        cooks = get_user_model().objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["cook_list"]), list(cooks))
        self.assertTemplateUsed(response, "kitchen/cook_list.html")

    def test_create_cook(self):
        form_data = {
            "username": "testuser",
            "password1": "test12345",
            "password2": "test12345",
            "first_name": "Test First",
            "last_name": "Test Last",
            "years_of_experience": 10
        }
        self.client.post(reverse("kitchen:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(
            new_user.years_of_experience,
            form_data["years_of_experience"]
        )


class PublicDishesTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_required(self):
        response = self.client.get(DISHES_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateDishesTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test",
            password="user12345"
        )
        self.client.force_login(self.user)

    def test_retrieve_dishes(self):
        dish_type = DishType.objects.create(
            name="Desserts"
        )
        Dish.objects.create(name="Napoleon", dish_type=dish_type)

        response = self.client.get(DISHES_URL)
        dishes = Dish.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dish_list"]), list(dishes))
        self.assertTemplateUsed(response, "kitchen/dish_list.html")
