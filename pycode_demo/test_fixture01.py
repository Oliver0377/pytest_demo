import pytest

# 创建一个登陆的fixture方法
@pytest.fixture()
def login():
    print("登陆操作")
    print("获取token")
    username = "ilya"
    password = "123456"
    token = "token123456"
    yield [token]
    print("登出")


def test_case1(login):
    print("测试用例一，需要登陆")
    print(f"login token:{login}")


def test_case2(connectdb):
    print("测试用例二，不需要登陆")


@pytest.mark.usefixtures("login")
def test_case3():
    print("测试用例三，需要登陆")
