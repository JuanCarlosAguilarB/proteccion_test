from typing import List


def calculate_fibonacci_with_seed(seed1: int, seed2: int, n: int) -> List[int]:
    """
    Calculate the Fibonacci series with given seeds and length.

    Args:
    - seed1: The first seed value of the Fibonacci series.
    - seed2: The second seed value of the Fibonacci series.
    - n: The number of Fibonacci series elements to generate.

    Returns:
    - fibonacci_series: A list containing the Fibonacci series.

    Raises:
    - ValueError: If any of the input values (seed1, seed2, n) is less than or equal to 0.
    """

    if seed1 <= 0 or seed2 <= 0:
        raise ValueError(
            "Los valores de los términos de la serie de Fibonacci deben ser positivos" +
            f"seed1 = {seed1}, seed2 = {seed2}, n = {n}")

    fibonacci_series = [seed1, seed2]

    for _ in range(2, n):
        next_value = fibonacci_series[-1] + fibonacci_series[-2]
        fibonacci_series.append(next_value)

    return fibonacci_series
