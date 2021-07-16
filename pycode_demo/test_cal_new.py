import pytest


class TestCal1:

    @pytest.mark.run(order=1)
    def test_add(self, get_cal, get_adddatas):
        result = None
        try:
            result = get_cal.addnum(get_adddatas[0], get_adddatas[1])
            # 结果强制转换保留两位小数
            if isinstance(result, float):
                result = round(result, 2)
            print(f"结果是：{result}")
        except Exception as e:
            print(e)
        assert result == get_adddatas[2]

    @pytest.mark.run(order=3)
    def test_mul(self, get_cal, get_muldatas):
        result = None
        try:
            result = get_cal.mulnum(get_muldatas[0], get_muldatas[1])
            if isinstance(result, float):
                result = round(result, 2)
            print(f"结果是：{result}")
        except Exception as e:
            print(e)
        assert result == get_muldatas[2]

    @pytest.mark.run(order=4)
    def test_div(self, get_cal, get_divdatas):
        result = None
        try:
            result = get_cal.divnum(get_divdatas[0], get_divdatas[1])
            if isinstance(result, float):
                result = round(result, 2)
            print(f"结果是：{result}")
        except Exception as e:
            print(e)
        assert result == get_divdatas[2]

    @pytest.mark.run(order=2)
    def test_sub(self, get_cal, get_subdatas):
        result = None
        try:
            result = get_cal.subnum(get_subdatas[0], get_subdatas[1])
            if isinstance(result, float):
                result = round(result, 2)
            print(f"结果是：{result}")
        except Exception as e:
            print(e)
        assert result == get_subdatas[2]


if __name__ == '__main__':
    pytest.main()
