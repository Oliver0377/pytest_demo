import pytest
import yaml


class TestData:
    # @pytest.mark.parametrize("a,b", [(1, 2), (2, 3), (10, 20)])
    # pytest使用yaml参数化
    @pytest.mark.parametrize("a,b", yaml.safe_load(open("./data.yml")))
    def test_data(self, a, b):
        print(a+b)


    # def test_data1(self):
    #     print(a+b)
    #
    #
    # def test_data2(self):
    #     print(a+b)
