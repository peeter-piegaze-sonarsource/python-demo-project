from my_project import add


def test_deploy(tmp_path):
    assert add(2, 2) == 4
