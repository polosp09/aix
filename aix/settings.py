"""
Contributions to this module:
Miguel Sanda <msanda@arrobalytics.com>
Mando <mandonpolo@gmail.com>
"""
from decimal import Decimal

from django.conf import settings

MANDO_BILL_NUMBER_LENGTH = getattr(settings, 'MANDO_BILL_NUMBER_LENGTH', 10)
MANDO_INVOICE_NUMBER_LENGTH = getattr(settings, 'MANDO_INVOICE_NUMBER_LENGTH', 10)
MANDO_FORM_INPUT_CLASSES = getattr(settings, 'MANDO_FORM_INPUT_CLASSES', 'dexa-forms ')
MANDO_CURRENCY_SYMBOL = getattr(settings, 'MANDO_CURRENCY_SYMBOL', 'UGX.')
MANDO_SPACED_CURRENCY_SYMBOL = getattr(settings, 'MANDO_SPACED_CURRENCY_SYMBOL', False)
MANDO_SHOW_FEEDBACK_BUTTON = getattr(settings, 'MANDO_SHOW_FEEDBACK_BUTTON', False)
MANDO_FEEDBACK_EMAIL_LIST = getattr(settings, 'MANDO_FEEDBACK_EMAIL_LIST', [])
MANDO_FEEDBACK_FROM_EMAIL = getattr(settings, 'MANDO_FEEDBACK_FROM_EMAIL', None)
MANDO_VALIDATE_SCHEMAS_AT_RUNTIME = getattr(settings, 'MANDO_VALIDATE_SCHEMAS_AT_RUNTIME', False)
MANDO_LOGIN_URL = getattr(settings, 'MANDO_LOGIN_URL', settings.LOGIN_URL)

MANDO_TRANSACTION_MAX_TOLERANCE = getattr(settings,
                                                  'MANDO_TRANSACTION_MAX_TOLERANCE',
                                                  Decimal('0.02'))

MANDO_TRANSACTION_CORRECTION = getattr(settings,
                                               'MANDO_TRANSACTION_CORRECTION',
                                               Decimal('0.01'))

MANDO_FINANCIAL_ANALYSIS = {
    'ratios': {
        'current_ratio': {
            'good_incremental': True,
            'ranges': {
                'healthy': 2,
                'watch': 1,
                'warning': .5,
                'critical': .25
            }
        },
        'quick_ratio': {
            'good_incremental': True,
            'ranges': {
                'healthy': 2,
                'watch': 1,
                'warning': .5,
                'critical': .25
            }
        },
        'debt_to_equity': {
            'good_incremental': False,
            'ranges': {
                'healthy': 0,
                'watch': .25,
                'warning': .5,
                'critical': 1
            }
        },
        'return_on_equity': {
            'good_incremental': True,
            'ranges': {
                'healthy': .10,
                'watch': .07,
                'warning': .04,
                'critical': .02
            }
        },
        'return_on_assets': {
            'good_incremental': True,
            'ranges': {
                'healthy': .10,
                'watch': .06,
                'warning': .04,
                'critical': .02
            }
        },
        'net_profit_margin': {
            'good_incremental': True,
            'ranges': {
                'healthy': .10,
                'watch': .06,
                'warning': .04,
                'critical': .02
            }
        },
        'gross_profit_margin': {
            'good_incremental': True,
            'ranges': {
                'healthy': .10,
                'watch': .06,
                'warning': .04,
                'critical': .02
            }
        },
    }
}
