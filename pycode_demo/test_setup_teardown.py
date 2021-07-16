import pytest

def setup_module():
    print("\n模块执行前执行一次")


def teardown_module():
    print("\n模块执行后执行一次")


def setup_function():
    print("\n类外用例执行前")


def teardown_function():
    print("\n类外用例执行后")


def test_three():
    print("正在执行test_three")


def test_four():
        print("正在执行test_four")


class TestClass:

    def setup_class(self):
        print("\n所有用力执行前")

    def teardown_class(self):
        print("\n所有用力执行后")

    def setup_method(self):
        print("\n每个用力开始前执行")

    def teardown_method(self):
        print("\n每个用力结束后执行")

    def test_one(self):
        print("正在执行test_one")

    def test_two(self):
        print("正在执行test_two")
