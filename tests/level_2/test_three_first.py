from functions.level_2.three_first import first
import pytest


def test__first__items_have_value():
    assert first([1, 2, 3, 4]) == 1


def test__first__fails_on_empty_items_and_value_not_passed_to_default():
    with pytest.raises(AttributeError):
        first([])


def test__first__items_are_empty_and_value_passed_to_default():
    assert first([], 1) == 1
