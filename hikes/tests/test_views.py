import datetime

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from hikes.forms import (
    ExpeditionTitleSearchForm,
    RegionNameSearchForm,
    HikerUsernameSearchForm
)
from hikes.models import Region, Hiker, Expedition, DifficultyLevel

REGION_LIST_URL = reverse("hikes:region-list")
HIKER_LIST_URL = reverse("hikes:hiker-list")
EXPEDITION_LIST_URL = reverse("hikes:expedition-list")


class PublicAccessTest(TestCase):
    def test_login_required_for_all_protected_urls(self):
        urls_to_test = [
            REGION_LIST_URL,
            HIKER_LIST_URL,
            EXPEDITION_LIST_URL,
            reverse("hikes:index"),
            reverse("hikes:hiker-detail", kwargs={"pk": 1}),
            reverse("hikes:expedition-detail", kwargs={"pk": 1}),
            reverse("hikes:region-create"),
            reverse("hikes:region-update", kwargs={"pk": 1}),
            reverse("hikes:region-delete", kwargs={"pk": 1}),
            reverse("hikes:hiker-create"),
            reverse("hikes:hiker-update", kwargs={"pk": 1}),
            reverse("hikes:hiker-delete", kwargs={"pk": 1}),
            reverse("hikes:expedition-create"),
            reverse("hikes:expedition-update", kwargs={"pk": 1}),
            reverse("hikes:expedition-delete", kwargs={"pk": 1}),
            reverse(
                "hikes:expedition-toggle-participation",
                kwargs={"pk": 1}
            )
        ]

        for url in urls_to_test:
            with self.subTest(url=url):
                res = self.client.get(url)
                expected_redirect_url = f"/accounts/login/?next={url}"
                self.assertRedirects(res, expected_redirect_url)


class PrivateRegionTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password",
        )
        self.client.force_login(self.user)

    def test_retrieve_regions(self):
        Region.objects.create(
            name="test_region1",
            country="test_country1",
        )
        Region.objects.create(
            name="test_region2",
            country="test_country2",
        )
        res = self.client.get(REGION_LIST_URL)
        self.assertEqual(res.status_code, 200)
        regions = Region.objects.all()
        self.assertEqual(
            list(res.context["region_list"]),
            list(regions)
        )
        self.assertTemplateUsed(res, "hikes/region_list.html")


class PrivateHikerTest(TestCase):
    def setUp(self):
        self.hiker1 = get_user_model().objects.create_user(
            username="test_username1",
            password="test_password1",
            first_name="test_first_name1",
            last_name="test_last_name1",
            fitness_level="beginner",
            has_tent=True
        )
        self.client.force_login(self.hiker1)
        self.hiker2 = get_user_model().objects.create_user(
            username="test_username2",
            password="test_password2",
            first_name="test_first_name2",
            last_name="test_last_name2",
            fitness_level="beginner",
            has_tent=True
        )

    def test_retrieve_hikers(self):
        res = self.client.get(HIKER_LIST_URL)
        self.assertEqual(res.status_code, 200)
        hikers = Hiker.objects.all()
        self.assertEqual(
            list(res.context["hiker_list"]),
            list(hikers)
        )
        self.assertTemplateUsed(res, "hikes/hiker_list.html")


class PrivateExpeditionTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password",
        )
        self.client.force_login(self.user)
        self.difficulty_level = DifficultyLevel.objects.create(name="test")
        self.region = Region.objects.create(
            name="test_name",
            country="test_country"
        )
        self.expedition1 = Expedition.objects.create(
            title="test_title1",
            description="test_description1",
            date=datetime.date.today(),
            difficulty=self.difficulty_level,
            region=self.region,
        )
        self.expedition2 = Expedition.objects.create(
            title="test_title2",
            description="test_description2",
            date=datetime.date.today(),
            difficulty=self.difficulty_level,
            region=self.region,
        )

    def test_retrieve_expeditions(self):
        res = self.client.get(EXPEDITION_LIST_URL)
        self.assertEqual(res.status_code, 200)
        expeditions = Expedition.objects.all()
        self.assertEqual(
            list(res.context["expedition_list"]),
            list(expeditions)
        )
        self.assertTemplateUsed(res, "hikes/expedition_list.html")


class PrivateIndexTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password",
        )
        self.client.force_login(self.user)

    def test_retrieve_index(self):
        res = self.client.get(reverse("hikes:index"))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, "hikes/index.html")

    def test_count_visit(self):
        url = reverse("hikes:index")
        res = self.client.get(url)
        self.assertEqual(res.context["num_visits"], 1)
        res = self.client.get(url)
        self.assertEqual(res.context["num_visits"], 2)


class PrivateExpeditionAssignTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="",
        )
        self.client.force_login(self.user)
        self.region = Region.objects.create(
            name="test_region",
            country="test_country"
        )
        self.difficulty_level = DifficultyLevel.objects.create(name="test")
        self.expedition = Expedition.objects.create(
            title="test_title",
            description="test_description",
            date=datetime.date.today(),
            difficulty=self.difficulty_level,
            region=self.region,
        )

    def test_assign_hiker_to_expedition(self):
        url = reverse(
            "hikes:expedition-toggle-participation",
            args=[self.expedition.id]
        )
        res = self.client.get(url)
        expected_url = reverse(
            "hikes:expedition-detail",
            args=[self.expedition.id]
        )
        self.assertRedirects(res, expected_url)
        self.assertIn(self.expedition, self.user.expeditions.all())

    def test_remove_hiker_from_expedition(self):
        self.user.expeditions.add(self.expedition)
        url = reverse(
            "hikes:expedition-toggle-participation",
            args=[self.expedition.id]
        )
        res = self.client.get(url)
        expected_url = reverse(
            "hikes:expedition-detail",
            args=[self.expedition.id]
        )
        self.assertRedirects(res, expected_url)
        self.assertNotIn(self.expedition, self.user.expeditions.all())


class PrivateExpeditionSearchTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password",
        )
        self.client.force_login(self.user)
        self.region = Region.objects.create(
            name="test_region",
            country="test_country"
        )
        self.difficulty_level = DifficultyLevel.objects.create(
            name="test_difficulty_level"
        )
        self.expedition1 = Expedition.objects.create(
            title="test1_title1",
            description="test_description1",
            date=datetime.date.today(),
            difficulty=self.difficulty_level,
            region=self.region,
        )
        self.expedition2 = Expedition.objects.create(
            title="test2_title2",
            description="test_description2",
            date=datetime.date.today(),
            difficulty=self.difficulty_level,
            region=self.region,
        )

    def test_search_form_in_context(self):
        res = self.client.get(EXPEDITION_LIST_URL)
        self.assertEqual(res.status_code, 200)
        self.assertIn("search_form", res.context)
        self.assertIsInstance(
            res.context["search_form"], ExpeditionTitleSearchForm
        )

    def test_search_without_parameters_returns_all(self):
        res = self.client.get(EXPEDITION_LIST_URL, {"title": ""})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context["expedition_list"]), 2)
        self.assertIn(self.expedition1, res.context["expedition_list"])
        self.assertIn(self.expedition2, res.context["expedition_list"])

    def test_successful_search_by_title(self):
        res = self.client.get(EXPEDITION_LIST_URL, {"title": "test1"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context["expedition_list"]), 1)
        self.assertIn(self.expedition1, res.context["expedition_list"])
        self.assertNotIn(self.expedition2, res.context["expedition_list"])

    def test_search_with_no_results(self):
        res = self.client.get(EXPEDITION_LIST_URL, {"title": "V"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context["expedition_list"]), 0)


class PrivateRegionSearchTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test_password",
        )
        self.client.force_login(self.user)
        self.region_lviv = Region.objects.create(
            name="Lviv",
            country="Ukraine"
        )
        self.region_lutsk = Region.objects.create(
            name="Lutsk",
            country="Ukraine"
        )

    def test_search_form_in_context(self):
        res = self.client.get(REGION_LIST_URL)
        self.assertEqual(res.status_code, 200)
        self.assertIn("search_form", res.context)
        self.assertIsInstance(
            res.context["search_form"],
            RegionNameSearchForm
        )

    def test_search_without_parameters_returns_all(self):
        res = self.client.get(REGION_LIST_URL, {"name": ""})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context["region_list"]), 2)
        self.assertIn(
            self.region_lviv,
            res.context["region_list"]
        )
        self.assertIn(
            self.region_lutsk,
            res.context["region_list"]
        )

    def test_successful_search_by_name(self):
        res = self.client.get(REGION_LIST_URL, {"name": "Lvi"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context["region_list"]), 1)
        self.assertIn(
            self.region_lviv,
            res.context["region_list"]
        )
        self.assertNotIn(
            self.region_lutsk,
            res.context["region_list"]
        )

    def test_search_with_no_results(self):
        res = self.client.get(REGION_LIST_URL, {"name": "Kyiv"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context["region_list"]), 0)


class PrivateHikerSearchTest(TestCase):
    def setUp(self):
        self.hiker_joyce = get_user_model().objects.create_user(
            username="joyce.byers",
            password="",
            first_name="Joyce",
            last_name="Byers",
        )
        self.client.force_login(self.hiker_joyce)
        self.hiker_jim = get_user_model().objects.create_user(
            username="jim.hopper",
            password="",
            first_name="Jim",
            last_name="Hopper",
        )

    def test_search_form_in_context(self):
        res = self.client.get(HIKER_LIST_URL)
        self.assertEqual(res.status_code, 200)
        self.assertIn("search_form", res.context)
        self.assertIsInstance(
            res.context["search_form"],
            HikerUsernameSearchForm
        )

    def test_search_without_parameters_returns_all(self):
        res = self.client.get(HIKER_LIST_URL, {"username": ""})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context["hiker_list"]), 2)
        self.assertIn(self.hiker_joyce, res.context["hiker_list"])
        self.assertIn(self.hiker_jim, res.context["hiker_list"])

    def test_successful_search_by_username(self):
        res = self.client.get(HIKER_LIST_URL, {"username": "jim"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context["hiker_list"]), 1)
        self.assertIn(self.hiker_jim, res.context["hiker_list"])
        self.assertNotIn(self.hiker_joyce, res.context["hiker_list"])

    def test_search_with_no_results(self):
        res = self.client.get(HIKER_LIST_URL, {"username": "mariia"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.context["hiker_list"]), 0)
        self.assertNotIn(self.hiker_joyce, res.context["hiker_list"])
        self.assertNotIn(self.hiker_jim, res.context["hiker_list"])
