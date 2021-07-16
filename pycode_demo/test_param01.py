import pytest


@pytest.mark.parametrize("a", [0, 1])
@pytest.mark.parametrize("b", [2, 3])
def test_foo(a, b):
    print(f"测试参数堆叠组合：a={a},b={b}")
