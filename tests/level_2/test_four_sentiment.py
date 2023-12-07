from functions.level_2.four_sentiment import check_tweet_sentiment
import pytest


@pytest.mark.parametrize(
    'text, good_words, bad_words, expected_result',
    [
        pytest.param(
            'hate love good bad',
            {'love', 'good'},
            {'hate', 'bad'},
            None,
            id='good words num equal bad words num'
        ),
        pytest.param(
            '',
            {'love', 'good'},
            {'hate', 'bad'},
            None,
            id='no good words and no bad words'
        )
    ]
)
def test__check_tweet_sentiment__return_none(text, good_words, bad_words, expected_result):
    assert check_tweet_sentiment(text, good_words, bad_words) is expected_result


def test__check_tweet_sentiment__good_words_num_more_than_bad_words_num():
    assert check_tweet_sentiment(
        text='love good bad',
        good_words={'love', 'good'},
        bad_words={'hate', 'bad'}
    ) == 'GOOD'


def test__check_tweet_sentiment__bad_words_num_more_than_good_words_num():
    assert check_tweet_sentiment(
        text='love hate bad',
        good_words={'love', 'good'},
        bad_words={'hate', 'bad'}
    ) == 'BAD'
