import random
import pytest
import string


@pytest.fixture(scope='class')
def random_value():
    yield random.randint(1, 1000)


@pytest.fixture()
def random_string():
    def rand_str(n): return ''.join(
        [random.choice(string.ascii_lowercase) for i in range(n)])
    yield rand_str(10)
