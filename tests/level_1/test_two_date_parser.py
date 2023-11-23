from freezegun import freeze_time
from functions.level_1.two_date_parser import compose_datetime_from
from datetime import datetime
import pytest


@freeze_time('2023-11-19')
def test__compose_datetime_from__tomorrow_date():
    assert compose_datetime_from(date_str='tomorrow', time_str='21:12') == datetime(
        year=2023,
        month=11,
        day=20,
        hour=21,
        minute=12
    )


@freeze_time('2023-11-19')
@pytest.mark.parametrize(
    'date_str, time_str, expected_result',
    [
        pytest.param(
            '',
            '21:12',
            datetime(year=2023, month=11, day=19, hour=21, minute=12),
            id='date_str is empty'
        ),
        pytest.param(
            'today',
            '21:12',
            datetime(year=2023, month=11, day=19, hour=21, minute=12),
            id='date_str is not empty'
        ),
    ]
)
def test__compose_datetime_from__today_date(date_str, time_str, expected_result):
    assert compose_datetime_from(date_str, time_str) == expected_result


@freeze_time('2023-11-19')
def test__compose_datetime_from__fails_on_empty_time_str():
    with pytest.raises(ValueError):
        compose_datetime_from(date_str='tomorrow', time_str='')


@freeze_time('2023-11-19')
def test__compose_datetime_from__fails_on_incorrect_time_str():
    with pytest.raises(ValueError):
        compose_datetime_from(date_str='tomorrow', time_str='21.12')
