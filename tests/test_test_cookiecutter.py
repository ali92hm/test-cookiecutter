from test_cookiecutter import test_cookiecutter


def test_add():
    res = test_cookiecutter.add(2, 3)
    assert res == 5
