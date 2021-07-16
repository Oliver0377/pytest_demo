import os

import yaml

import pytest

from pycode_demo.python_dev_code.calculator import Cal


yamlfile = os.path.dirname(__file__) + "/test_counter.yml"


with open(yamlfile, encoding="utf-8") as num:
    data = yaml.safe_load(num)
    adddata = data["add_datas"]
    subdata = data["sub_datas"]
    muldata = data["mul_datas"]
    divdata = data["div_datas"]


@pytest.fixture(params=adddata, scope="module")
def get_adddatas(request):
    print("开始计算")
    addtestdata = request.param
    print(f"加法测试数据是{addtestdata}")
    yield addtestdata
    print("结束计算")


@pytest.fixture(params=subdata, scope="module")
def get_subdatas(request):
    print("开始计算")
    subtestdata = request.param
    print(f"减法测试数据是{subtestdata}")
    yield subtestdata
    print("结束计算")


@pytest.fixture(params=muldata, scope="module")
def get_muldatas(request):
    print("开始计算")
    multestdata = request.param
    print(f"乘法测试数据是{multestdata}")
    yield multestdata
    print("结束计算")


@pytest.fixture(params=divdata, scope="module")
def get_divdatas(request):
    print("开始计算")
    divtestdata = request.param
    print(f"除法测试数据是{divtestdata}")
    yield divtestdata
    print("结束计算")


@pytest.fixture(scope="session")
def connectdb():
    print("连接数据库")
    yield
    print("断开数据库")


@pytest.fixture(scope="module")
def get_cal():
    print("获取计算机实例")
    cal = Cal()
    return cal
