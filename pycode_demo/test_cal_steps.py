import yaml
import pytest
from pycode_demo.test_cal import TestCal


def test_steps(path):
    with open(path, encoding="utf-8") as steps_data:
        testcal_steps = yaml.safe_load(steps_data)
    if "test_add" in testcal_steps:
        TestCal.test_add()
    if "test_sub" in testcal_steps:
        TestCal.test_sub()
    if "test_mul" in testcal_steps:
        TestCal.test_mul()
    if "test_div" in testcal_steps:
        TestCal.test_div()


def test_internet():
    test_steps("test_calsteps.yml")
