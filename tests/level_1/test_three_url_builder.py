from functions.level_1.three_url_builder import build_url


def test__build_url__passed_all_parameters():
    assert build_url(
        host_name='englishfootball',
        relative_url='premierleague',
        get_params={'team': 'chelsea', 'player': 'lampard'}
    ) == 'englishfootball/premierleague?team=chelsea&player=lampard'


def test__build_url__get_params_is_none():
    assert build_url(
        host_name='englishfootball',
        relative_url='premierleague',
    ) == 'englishfootball/premierleague'


def test__build_url__get_params_has_different_types():
    assert build_url(
        host_name=5,
        relative_url='premierleague',
        get_params={'team': 1, 'player': 'lampard'}
    ) == '5/premierleague?team=1&player=lampard'


def test__build_url__host_name_is_empty():
    assert build_url(
        host_name='',
        relative_url='premierleague',
        get_params={'team': 'chelsea', 'player': 'lampard'}
    ) == '/premierleague?team=chelsea&player=lampard'


def test__build_url__host_name_type_is_int():
    assert build_url(
        host_name=5,
        relative_url='premierleague',
        get_params={'team': 'chelsea', 'player': 'lampard'}
    ) == '5/premierleague?team=chelsea&player=lampard'


def test__build_url__relative_url_is_empty():
    assert build_url(
        host_name='',
        relative_url='premierleague',
        get_params={'team': 'chelsea', 'player': 'lampard'}
    ) == '/premierleague?team=chelsea&player=lampard'
