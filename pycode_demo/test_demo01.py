import pytest


def inc(x):
    return x + 1

# pytest参数化
@pytest.mark.parametrize('a,b', [
        (1, 2),
        (10, 20),
        ('a', 'a1')
    ])
def test_answer(a, b):
    assert inc(a) == b


def test_answer1():
    assert inc(4) == 5


@pytest.fixture()
def login():
    print("登录操作")
    username = "Ilya"
    return username


class TestDemo:
    def test_a(self,login):
        print(f"a username={login}")

    def test_b(self):
        print("b")


if __name__ == "__main__":
    pytest.main(['test_demo01.py::TestDemo', '-v'])
