import allure
import pytest


def test_attach_text():
    allure.attach("这是一个纯文本", attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<body>这是一个HTMLBody块</body>", "html测试块", attachment_type=allure.attachment_type.HTML)


def test_attach_photo():
    allure.attach.file("C:/Users/16587/Desktop/f2d236222e4eda09720a58bd8c399e74.jpg", name="图片", attachment_type=allure.attachment_type.JPG)


if __name__ == "__main__":
    pytest.main()
