import pytest
from algorithms.find_min_max import min_max


@pytest.fixture
def input_data() -> list[int]:
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_min_max(input_data: list[int]) -> None:
    res = min_max(input_data)
    assert "Min: 1, Max: 10" == res
