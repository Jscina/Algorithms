import math
import random
import pytest
from algorithms.dyn_prog_factorial import factorial


@pytest.fixture
def rand_cases() -> list[int]:
    return [random.randint(0, 100) for _ in range(10)]


def test_factorial(rand_cases: list[int]):
    for case in rand_cases:
        assert factorial(case) == math.factorial(case)
