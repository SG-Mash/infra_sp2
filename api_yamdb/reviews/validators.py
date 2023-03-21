from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year(value):
    if timezone.now().year < value:
        raise ValidationError(
            "Год произведения не может быть больше текущего!"
        )
