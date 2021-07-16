import pytest


class Test_real01:
    @pytest.mark.smoke
    def test_one(self):
        assert 1 == 1

    @pytest.mark.demo
    def test_two(self):
        assert 1 == 2

    @pytest.mark.play
    def test_three(self):
        assert 1 == 3
