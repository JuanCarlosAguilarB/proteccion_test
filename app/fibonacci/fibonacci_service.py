from .fibonaci_calculate import calculate_fibonacci_with_seed
from typing import List


def reverse_fibonacci_serie(seed1: int, seed2: int, n: int) -> List[int]:
    """
        Generate the reverse Fibonacci series with given seeds and length.

        Args:
        - seed1: The first seed value of the Fibonacci series.
        - seed2: The second seed value of the Fibonacci series.
        - n: The number of Fibonacci series elements to generate.

        Returns:
        - reversed_fibonacci_series: A list containing the reverse Fibonacci series.

        Raises:
        - ValueError: If any of the input values (seed1, seed2, n) is less than or equal to 0.
    """
    fibonacci_series = calculate_fibonacci_with_seed(seed1, seed2, n + 2)
    return fibonacci_series[::-1]
