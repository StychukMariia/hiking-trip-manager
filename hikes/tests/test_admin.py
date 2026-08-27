from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="test_admin",
            password="test_password",
        )
        self.client.force_login(self.admin_user)
        self.hiker = get_user_model().objects.create_user(
            username="test_username",
            password="test_password",
            fitness_level="beginner",
            has_tent=False
        )

    def test_hiker_fitness_level_listed(self):
        url = reverse("admin:hikes_hiker_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.hiker.get_fitness_level_display())

    def test_hiker_detail_fitness_level_listed(self):
        url = reverse("admin:hikes_hiker_change", args=[self.hiker.id])
        res = self.client.get(url)
        self.assertContains(res, self.hiker.fitness_level)

    def test_hiker_add_fitness_level_listed(self):
        url = reverse("admin:hikes_hiker_add")
        res = self.client.get(url)
        self.assertContains(res, "fitness_level")

    def test_hiker_has_tent_listed(self):
        url = reverse("admin:hikes_hiker_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.hiker.has_tent)

    def test_hiker_detail_has_tent_listed(self):
        url = reverse("admin:hikes_hiker_change", args=[self.hiker.id])
        res = self.client.get(url)
        self.assertContains(res, 'name="has_tent"')

    def test_hiker_add_has_tent_listed(self):
        url = reverse("admin:hikes_hiker_add")
        res = self.client.get(url)
        self.assertContains(res, "has_tent")
