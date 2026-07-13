from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class DifficultyLevel(models.Model):
    name = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.country})"


class Hiker(AbstractUser):
    FITNESS_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
        ('expert', 'Expert'),
    )

    fitness_level = models.CharField(
        max_length=20,
        choices=FITNESS_CHOICES,
        default='beginner'
    )
    has_tent = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Hiker"
        verbose_name_plural = "Hikers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("hikes:hiker-detail", kwargs={"pk": self.pk})
