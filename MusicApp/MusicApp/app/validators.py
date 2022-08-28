from django.core.exceptions import ValidationError


def only_letters_numbers_underscore_validator(input):
    for ch in input:
        if ch.isalpha() or ch.isdigit() or ch == '_':
            continue
        else:
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
