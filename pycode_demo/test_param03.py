import pytest
import yaml


def step1():
    print("\n打开页面")


def step2():
    print("注册用户")


def step3():
    print("登录")


# 根据需求将测试用例封装为步骤方法，通过读取yaml文件里步骤进行执行
def steps(path):
    with open(path) as steps_data:
        testlogin_steps = yaml.safe_load(steps_data)
    if "step1" in testlogin_steps:
        step1()
    if "step2" in testlogin_steps:
        step2()
    if "step3" in testlogin_steps:
        step3()


def test_login_internet():
    steps("./pycode_demo/test_steps.yml")
