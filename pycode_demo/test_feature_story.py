import pytest
import allure


# 标记模块名
@allure.severity(allure.severity_level.NORMAL)
@allure.feature("登录模块")
class TestLogin:
    # 标记方法名
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登陆：测试用例，登陆成功")
        pass

    @allure.severity(allure.severity_level.MINOR)
    @allure.story("登陆失败")
    def test_login_success_a(self):
        print("这是登录：测试用例，登陆成功")
        pass

    @allure.story("用户名缺失")
    def test_login_unusername(self):
        print("用户名缺失")
        pass

    @allure.story("密码缺失")
    def test_login_unpassword(self):
        # 标记步骤名
        with allure.step("点击用户名"):
            print("输入用户名")
        with allure.step("点击密码"):
            print("输入密码")
        print("点击登录")
        with allure.step("点击登录后失败"):
            assert "1" == 1
            print("登录失败")
        pass

    @allure.story("登录失败")
    def test_login_defeat(self):
        print("这是登录：测试用例，登陆失败")
        pass


if __name__ == "__main__":
    pytest.main()
