import pytest
import sys


class TestSampleA:

    @pytest.mark.skip(reason="Database is not setup yet")
    def test_a(self):
        print("This is Test A")

    @pytest.mark.skipif(sys.platform == "darwin", reason="Skip test for Mac OS")
    def test_b(self):
        print("This is Test B")

    @pytest.mark.skip_test_if_env('prod')
    def test_c(self):
        print("This is Test C")

    def test_d(self):
        print("This is Test D")

    def test_e(self):
        print("This is Test E")
