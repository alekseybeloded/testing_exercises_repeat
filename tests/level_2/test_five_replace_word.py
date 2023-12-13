from functions.level_2.five_replace_word import replace_word


def test__replace_word__return_new_text():
    assert replace_word(
        text='Old text',
        replace_from='old',
        replace_to='New'
    ) == 'New text'


def test__replace_word__return_old_text():
    assert replace_word(
        text='Example text',
        replace_from='old',
        replace_to='New'
    ) == 'Example text'
