from functions.level_1.five_title import change_copy_item


def test__change_copy_item__title_is_not_equal_additional_copy_text_and_title_has_len_less_than_max_main_item_title_length():
    assert change_copy_item(title='Daily news') == 'Copy of Daily news'


def test__change_copy_item__len_title_with_additional_copy_text_more_or_equal_max_main_item_title_length():
    assert change_copy_item(title='New enimals in the Moscow zoo', max_main_item_title_length=20) == 'New enimals in the Moscow zoo'


def test__change_copy_item__title_has_not_copy_number():
    assert change_copy_item(title='Copy of') == 'Copy of (2)'


def test__change_copy_item__title_has_copy_number():
    assert change_copy_item(title='Copy of (2)') == 'Copy of (3)'
