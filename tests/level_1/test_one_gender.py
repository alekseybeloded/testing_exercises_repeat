from functions.level_1.one_gender import genderalize
import pytest


def test__genderalize__return_verb_male():
    assert genderalize(verb_male='male', verb_female='female', gender='male') == 'male'


@pytest.mark.parametrize(
    'verb_male, verb_female, gender, expected_result',
    [
        pytest.param('male', 'female', '', 'female', id='gender is empty'),
        pytest.param('male', 'female', 'abc', 'female', id='gender is not equal "male"'),
    ]
)
def test__genderalize__return_verb_female(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) == expected_result
