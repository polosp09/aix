"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""

from django.core.exceptions import ValidationError


class InvalidDateInputException(ValidationError):
    pass


class TransactionNotInBalanceException(ValidationError):
    pass
