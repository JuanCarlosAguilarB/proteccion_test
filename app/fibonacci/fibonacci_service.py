from .fibonaci_calculate import calculate_fibonacci_with_seed
from typing import List


def reverse_fibonacci_serie(seed1: int, seed2: int, n: int) -> List[int]:
    fibonacci_series = calculate_fibonacci_with_seed(seed1, seed2, n + 2)
    return fibonacci_series[::-1]
