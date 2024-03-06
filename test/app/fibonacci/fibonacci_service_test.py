import pytest
from app.fibonacci.fibonacci_service import reverse_fibonacci_serie


def test_reverse_fibonacci_serie():
    # Test with valid inputs
    seed1 = 1
    seed2 = 1
    n = 4
    expected_result = [8, 5, 3, 2, 1, 1]
    assert reverse_fibonacci_serie(seed1, seed2, n) == expected_result

    # Test with negative seed values
    seed1 = -1
    seed2 = 1
    n = 4
    with pytest.raises(ValueError):
        reverse_fibonacci_serie(seed1, seed2, n)


    # Test with negative seed values
    seed1 = 1
    seed2 = -1
    n = 4
    with pytest.raises(ValueError):
        reverse_fibonacci_serie(seed1, seed2, n)
