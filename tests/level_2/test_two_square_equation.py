from functions.level_2.two_square_equation import solve_square_equation


def test__solve_square_equation__no_square_coefficient():
    assert solve_square_equation(0, 2.0, 2.0) == (-1, None)


def test__solve_square_equation__no_square_coefficient_and_no_linear_coefficient():
    assert solve_square_equation(0, 0, 2.0) == (None, None)


def test__solve_square_equation__discriminant_less_than_zero():
    assert solve_square_equation(2.5, 3.0, 3.0) == (None, None)


def test__solve_square_equation__has_two_roots():
    assert solve_square_equation(1.0, 3.0, 2.0) == (-2, -1)
