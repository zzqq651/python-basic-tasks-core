from misc.utils import calculate_square, calculate_average, is_prime
import pytest


@pytest.fixture(params=[1, 3])
def input_num(request):
    a = request.param
    return a


def test_calculate_square(input_num):
    result = calculate_square(input_num)

    assert result == input_num ** 2


@pytest.mark.parametrize("nums, expected_avg_num", (
    ([1, 2, 3], 2),
    ([3, 3, 3], 3),
))
def test_calculate_average(nums: list[int], expected_avg_num: int):
    result = calculate_average(nums)

    assert result == expected_avg_num


@pytest.mark.parametrize("num, expected_res", (
    (2, True),
    (3, True),
    (4, False),
    (49, False)
))
def test_is_prime(num: int, expected_res: bool):
    result = is_prime(num)

    assert result == expected_res
