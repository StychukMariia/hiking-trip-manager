from django.test import TestCase

from hikes.forms import HikerCreationForm, ExpeditionForm
from hikes.models import DifficultyLevel, Region, Hiker


class HikerCreationFormTest(TestCase):
    def test_hiker_creation_form_valid(self):
        data = {
            "username": "test_username",
            "first_name": "test_first_name",
            "last_name": "test_last_name",
            "fitness_level": "beginner",
            "has_tent": True,
            "password1": "5p1a8s9s3",
            "password2": "5p1a8s9s3",
        }
        form = HikerCreationForm(data=data)
        self.assertTrue(form.is_valid())


class ExpeditionFormTest(TestCase):
    def setUp(self):
        self.diff = DifficultyLevel.objects.create(name="Easy")
        self.reg = Region.objects.create(name="Lutsk", country="Ukraine")
        self.hiker = Hiker.objects.create_user(username="hiker1")

    def test_expedition_form_valid(self):
        data = {
            "title": "Mountain Trip",
            "difficulty": self.diff.id,
            "region": self.reg.id,
            "hikers": [self.hiker.id],
        }
        form = ExpeditionForm(data=data)
        self.assertTrue(form.is_valid())
