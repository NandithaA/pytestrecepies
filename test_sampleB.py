import pytest
import sys

pytestmark = pytest.mark.skipif(sys.version_info.major < 3, reason="Skip the test for python version 2 or less")


def test_a():
    print("This is Test A")


def test_b():
    print("This is Test B")


def test_c():
    print("This is Test C")


def test_d():
    print("This is Test D")


def test_e():
    print("This is Test E")
