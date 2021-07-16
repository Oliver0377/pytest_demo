import pytest
import yaml


# 将读取yaml文件操作封装为一个函数
def get_data():
    with open("./pycode_demo/param_data.yml") as yml:
        data = yaml.safe_load(yml)
        print(data)
        add_data = data["datas"]
        add_myids = data["myids"]
        return [add_data, add_myids]


def add_function(a, b):
    return a+b


@pytest.mark.parametrize("a, b, expected",
                         get_data()[0],
                         ids=get_data()[1])
def test_add(a, b, expected):
    assert add_function(a, b) == expected
