from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request_url__return_true():
    assert is_github_pull_request_url(
        'https://github.com/alekseybeloded/django_views_challenges/pull/2'
    ) is True


def test__is_github_pull_request_url__return_false():
    assert is_github_pull_request_url(
        'https://github.com/alekseybeloded/django_views_challenges/'
    ) is False
