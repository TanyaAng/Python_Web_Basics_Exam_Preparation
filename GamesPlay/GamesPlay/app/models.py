from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Profile(models.Model):
    MIN_AGE = 12
    PASSWORD_MAX_LENGHT = 30
    FIRST_NAME_MAX_LENGHT = 30
    LAST_NAME_MAX_LENGHT = 30

    email = models.EmailField()

    age = models.IntegerField(
        validators=(MinValueValidator(MIN_AGE),),
    )

    password = models.CharField(
        max_length=PASSWORD_MAX_LENGHT,
    )

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGHT,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGHT,
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
    TITLE_MAX_LENGHT = 30
    CATEGORY_MAX_LENGHT = 15
    RATING_MIN_VALUE = 0.1
    RATING_MAX_VALUE = 5.0
    LEVEL_MIN_VALUE = 1

    CATEGORY_TYPE = ('Action', 'Adventure', 'Puzzle', 'Strategy', 'Sports', 'Board/Card Game', 'Other')
    CATEGORY_CHOICES = [(f'{choice}', f'{choice}') for choice in CATEGORY_TYPE]

    title = models.CharField(
        max_length=TITLE_MAX_LENGHT,
        unique=True,
    )

    category = models.CharField(
        max_length=CATEGORY_MAX_LENGHT,
        choices=CATEGORY_CHOICES
    )

    rating = models.FloatField(
        validators=(MinValueValidator(RATING_MIN_VALUE),
                    MaxValueValidator(RATING_MAX_VALUE),
                    )
    )

    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(MinValueValidator(LEVEL_MIN_VALUE),
                    )
    )

    image_url = models.URLField()

    summary = models.TextField(
        null=True,
        blank=True,
    )
