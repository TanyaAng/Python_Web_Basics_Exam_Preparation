from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator

from MusicApp.app.validators import only_letters_numbers_underscore_validator


class Profile(models.Model):
    USERNAME_MAX_LENGTH = 15
    USERNAME_MIN_LENGTH = 2
    AGE_MIN_VALUE = 0

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        validators=(MinLengthValidator(USERNAME_MIN_LENGTH), only_letters_numbers_underscore_validator)
    )
    email = models.EmailField()

    age = models.IntegerField(
        validators=(MinValueValidator(AGE_MIN_VALUE),
                    ),
        null=True,
        blank=True,
    )


class Album(models.Model):
    ALBUM_NAME_MAX_LENGTH = 30
    ARTIST_NAME_MAX_LENGTH = 30
    GENRE_MAX_LENGTH = 30
    GENRE_TYPES = (
        "Pop Music", "Jazz Music", "R&B Music", "Rock Music", "Country Music", "Dance Music", "Hip Hop Music", "Other")
    GENRE_CHOICES = [(f'{type}', f'{type}') for type in GENRE_TYPES]
    PRICE_MIN_VALUE = 0

    album_name = models.CharField(
        unique=True,
        max_length=ALBUM_NAME_MAX_LENGTH,
        verbose_name='Album Name',
    )

    artist = models.CharField(
        max_length=ARTIST_NAME_MAX_LENGTH,
        verbose_name='Artist',
    )

    genre = models.CharField(
        max_length=GENRE_MAX_LENGTH,
        choices=GENRE_CHOICES,
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Description',
    )
    image_url = models.URLField(
        verbose_name='Image URL',
    )

    price = models.FloatField(
        validators=(MinValueValidator(PRICE_MIN_VALUE),),
        verbose_name='Price',
    )
