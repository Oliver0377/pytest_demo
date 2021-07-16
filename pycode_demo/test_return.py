from time import sleep

import pytest


def test_return():
    assert 2 == 2


def test_return1():
    assert 1 == 1


# @pytest.mark.flaky(reruns=5, reruns_deley=1)
def test_return2():
    assert 3 == 3


def test_return3():
    assert 4 == 4
