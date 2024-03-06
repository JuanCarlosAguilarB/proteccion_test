from typing import List


def calculate_fibonacci_with_seed(seed1: int, seed2: int, n: int) -> List[int]:
    fibonacci_series = [seed1, seed2]

    for _ in range(2, n):
        next_value = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_value)

    return fibonacci_series
