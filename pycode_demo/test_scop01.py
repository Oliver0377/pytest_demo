import pytest


# @pytest.fixture(scope="module")
# def connectdb():
#     print("连接数据库")
#     yield
#     print("断开数据库")


class TestDemo:

    def test_a(self, connectdb):
        print("测试用例a")

    def test_b(self, connectdb):
        print("测试用例b")


class TestDemo01:

    def test_a(self, connectdb):
        print("测试用例a")

    def test_b(self, connectdb):
        print("测试用例b")
