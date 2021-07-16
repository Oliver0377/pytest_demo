import os

from pycode_demo.python_dev_code.calculator import Cal
import pytest
import yaml

yamlfile = os.path.dirname(__file__) + "/test_counter.yml"
def get_testdatas():
    with open(yamlfile, encoding="utf-8") as num:
        data = yaml.safe_load(num)
        adddata = data["add_datas"]
        subdata = data["sub_datas"]
        muldata = data["mul_datas"]
        divdata = data["div_datas"]
        return [adddata, subdata, muldata, divdata]


class TestCal:
    def setup_class(self):
        self.cal = Cal()
        print("\n测试开始")

    def teardown_class(self):
        print("\n测试结束")

    def setup_method(self):
        print("\n计算开始")

    def teardown_method(self):
        print("\n计算结束")

    @pytest.mark.parametrize("a,b,expect",
                             get_testdatas()[0])
    def test_add(self, a, b, expect):
        result1 = self.cal.addnum(a, b)
        assert result1 == expect

    @pytest.mark.parametrize("a,b,expect",
                             get_testdatas()[1])
    def test_sub(self, a, b, expect):
        result2 = self.cal.subnum(a, b)
        assert result2 == expect

    @pytest.mark.parametrize("a,b,expect",
                             get_testdatas()[2])
    def test_mul(self, a, b, expect):
        result3 = self.cal.mulnum(a, b)
        assert result3 == expect

    @pytest.mark.parametrize("a,b,expect",
                             get_testdatas()[3])
    def test_div(self, a, b, expect):
        result4 = self.cal.divnum(a, b)
        assert result4 == expect

