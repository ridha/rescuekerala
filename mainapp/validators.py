from django.core.exceptions import ValidationError
from phonenumbers import parse as phonenumber_parse
from phonenumbers import is_valid_number, NumberParseException


def validate_phonenumber(phonenumber) -> None:
    try:
        if not phonenumber:
            return
        num_obj = phonenumber_parse(phonenumber, region="IN")
        if not is_valid_number(num_obj):
            raise ValidationError("The phone number entered is not valid.",
                                  code="invalid_phone_number")
    except NumberParseException:
        raise ValidationError("The phone number entered is not valid.",
                              code="invalid_phone_number")
