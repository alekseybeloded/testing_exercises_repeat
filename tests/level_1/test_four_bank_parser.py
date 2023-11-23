from functions.level_1.four_bank_parser import BankCard, SmsMessage, parse_ineco_expense
import datetime
from decimal import Decimal
from functions.level_1.four_bank_parser import Expense
import pytest


def test__parse_ineco_expense__passed_all_parameters_with_correct_format():
    sms = SmsMessage(
        text='500 RUB, 1234 19.11.23 12:15 pyaterochka authcode ',
        author='sber',
        sent_at=datetime.datetime.now()
    )
    card = BankCard('1234', 'Ivan Ivanov')

    actual_result = parse_ineco_expense(sms, [card])

    assert actual_result == Expense(
        amount=Decimal('500'),
        card=BankCard(last_digits='1234', owner='Ivan Ivanov'),
        spent_in='pyaterochka',
        spent_at=datetime.datetime(2023, 11, 19, 12, 15),
    )


def test__parse_ineco_expense__fails_on_empty_text():
    sms = SmsMessage(
        text='',
        author='sber',
        sent_at=datetime.datetime.now()
    )
    card = BankCard('1234', 'Ivan Ivanov')

    with pytest.raises(ValueError):
        parse_ineco_expense(sms, [card])


def test__parse_ineco_expense__fails_on_incorrect_sms():
    sms = SmsMessage(
        text='500 RUB, 123 19.11.23 12:15 pyaterochka authcode ',
        author='sber',
        sent_at=datetime.datetime.now()
    )
    card = BankCard('1234', 'Ivan Ivanov')

    with pytest.raises(IndexError):
        parse_ineco_expense(sms, [card])
