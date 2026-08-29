"""
Exercise: Monte Carlo Estimate of Pi
---------------------------------------
Randomly scatter points in a 2x2 square centered on the origin (-1 to 1 on both axes).
The fraction that land inside the inscribed unit circle, times 4, estimates pi.

Write `estimate_pi(num_points) -> float`.
Hint: a point (x, y) is inside the unit circle if x**2 + y**2 <= 1.

Try it yourself before peeking at solutions/tier2_ai_ml/ex03_monte_carlo_pi.py.
"""

import random


def estimate_pi(num_points: int) -> float:
    # TODO: sample num_points random (x, y) pairs in [-1, 1], count how many land
    # inside the unit circle, and return 4 * (inside / num_points)
    # raise NotImplementedError("estimate_pi is not implemented yet")
    inside = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside += 1
    return 4 * inside / num_points


if __name__ == "__main__":
    for n in (100, 1_000, 100_000):
        print(f"n={n:>7}: pi ~= {estimate_pi(n):.4f}")
