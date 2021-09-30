from test_cookiecutter_ali92hm import test_cookiecutter_ali92hm


def test_add_unit():
    res = test_cookiecutter_ali92hm.add(2, 3)
    assert res == 5
