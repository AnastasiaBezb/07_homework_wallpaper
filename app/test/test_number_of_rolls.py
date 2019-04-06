from app.lib import number_of_rolls


def test_rolls():
    expected = 7
    actual = number_of_rolls(5.0, 6.0, 2.75, 1.1, 10.0)
    assert expected == actual
