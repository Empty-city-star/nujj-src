# This is purely the result of trial and error.

import sys

class PyTest():
    """
    Running `$ python setup.py test' simply installs minimal requirements
    and runs the tests with no fancy stuff like parallel execution.

    """
    def run_tests(self):
        import pytest
        sys.exit(pytest.main(self.test_args))
