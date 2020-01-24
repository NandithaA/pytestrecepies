import pytest


def pytest_addoption(parser):
    """Adding command line option"""

    parser.addoption("--env", action="store", default="test",
                     help="my option: branch/test/stage")


def pytest_configure(config):
    """Register the custom markers"""

    config.addinivalue_line("markers", "skip_test_if_env(env): this mark skips the tests for the given env")


def pytest_runtest_setup(item):
    """Custom Marker"""

    env_names = [mark.args[0] for mark in item.iter_markers(name="skip_test_if_env")]
    if env_names:
        if item.config.getoption("--env") in env_names:
            pytest.skip("Test skipped because env is {!r}".format(env_names))
