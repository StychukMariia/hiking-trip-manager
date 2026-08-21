import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase

from hikes.models import DifficultyLevel, Region, Hiker, Expedition


class TestModel(TestCase):
    def test_difficulty_level_str(self):
        difficulty_level = DifficultyLevel.objects.create(name="test")
        self.assertEqual(str(difficulty_level), difficulty_level.name)

    def test_region_str(self):
        region = Region.objects.create(
            name="test_name",
            country="test_country"
        )
        self.assertEqual(str(region), f"{region.name} ({region.country})")

    def test_hiker_str(self):
        hiker = get_user_model().objects.create(
            username="test_username",
            password="test_password",
            first_name="test_first_name",
            last_name="test_last_name",
            fitness_level="beginner",
            has_tent = True
        )
        self.assertEqual(
            str(hiker),
            f"{hiker.username} ({hiker.first_name} {hiker.last_name})"
        )

    def test_expedition_str(self):
        difficulty_level = DifficultyLevel.objects.create(name="test")
        region = Region.objects.create(
            name="test_name",
            country="test_country"
        )
        expedition = Expedition.objects.create(
            title="test_title",
            description="test_description",
            date=datetime.date.today(),
            difficulty=difficulty_level,
            region=region,
        )
        self.assertEqual(str(expedition), expedition.title)

    def test_create_hiker_with_fitness_level_and_has_tent(self):
        username = "test_username"
        password = "test_password"
        fitness_level = "beginner"
        has_tent = True
        hiker = get_user_model().objects.create_user(
            username=username,
            password=password,
            fitness_level=fitness_level,
            has_tent = has_tent
        )
        self.assertEqual(hiker.username, username)
        self.assertEqual(hiker.fitness_level, fitness_level)
        self.assertEqual(hiker.has_tent, has_tent)
        self.assertTrue(hiker.check_password(password))

