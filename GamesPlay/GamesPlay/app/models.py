from django.db import models


class Profile(models.Model):
    email = models.EmailField()

    age = models.IntegerField()

    password = models.CharField(
        max_length=30,
    )

    first_name = models.CharField(
        max_length=30,
    )

    last_name = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Game(models.Model):
    title = models.CharField(
        max_length=30,
    )

    category = models.CharField(
        max_length=15,
    )

    rating = models.CharField()

    max_level = models.IntegerField(
        null=True,
        blank=True,
    )

    image_url = models.URLField()

    summary = models.TextField(
        null=True,
        blank=True,
    )
