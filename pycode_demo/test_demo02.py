import yaml

import pytest


class TestDemo02:
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def test_demo(self, env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的IP是", env["test"])
        elif "dev" in env:
            print("这是开发环境")
