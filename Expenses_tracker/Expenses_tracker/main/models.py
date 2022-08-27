from django.db import models

from django.core.validators import MinLengthValidator, MinValueValidator

from Expenses_tracker.main.validators import only_letters_validator, MaxFileSizeInMbValidator


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 15
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 15

    BUDGET_DEFAULT_VALUE = 0
    BUDGET_MIN_VALUE = 0

    IMAGE_MAX_SIZE_IN_MB = 5
    IMAGE_UPLOAD_TO_DIR = 'profiles/'

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator),
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(MinLengthValidator(
            LAST_NAME_MIN_LENGTH),
                    only_letters_validator),
    )

    budget = models.FloatField(
        default=BUDGET_DEFAULT_VALUE,
        validators=(
            MinValueValidator(BUDGET_MIN_VALUE),
        ),
    )

    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        # default='static/images/user.png',
        validators=(
            MaxFileSizeInMbValidator(IMAGE_MAX_SIZE_IN_MB),
        ),
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class Expense(models.Model):
    TITLE_MAX_SIZE = 30

    title = models.CharField(
        max_length=TITLE_MAX_SIZE,
    )

    image = models.URLField(
        #verbose_name='Link to Image'
    )

    price = models.FloatField()

    description = models.TextField(
        null=True,
        blank=True
    )

    '''ONE TO MANY RELATIONS'''
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        ordering = ('price',)
