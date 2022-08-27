from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE = f"Value must contain only letters"


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError(VALIDATE_ONLY_LETTERS_EXCEPTION_MESSAGE)


def max_size_image_validator(value):
    MAX_SIZE = 5
    filesize = value.file.size
    if filesize > MAX_SIZE * 1024 * 1024:
        raise ValidationError(f"Max file size is {MAX_SIZE}MB")

@deconstructible
class MaxFileSizeInMbValidator:
    def __init__(self, max_size):
        self.max_size = max_size

    def __call__(self, value):
        filesize = value.file.size
        if filesize > self.__mb_to_bytes(self.max_size):
            raise ValidationError(self.__get_exception_message())

    @staticmethod
    def __mb_to_bytes(value):
        return value * 1024 * 1024

    def __get_exception_message(self):
        return f"Max file size is {self.max_size:.2f}MB"
