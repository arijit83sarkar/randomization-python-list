"""
Exercise: Weight Initializer
------------------------------
Neural networks start with small random weights before training. Simulate this
with plain nested lists (no numpy needed here).

Write `init_weights(rows, cols, low=-0.5, high=0.5) -> list[list[float]]`
  - returns a nested list (rows x cols) of random floats in [low, high]

Try it yourself before peeking at solutions/tier2_ai_ml/ex02_weight_initializer.py.
"""

import random


def init_weights(
    rows: int, cols: int, low: float = -0.5, high: float = 0.5
) -> list[list[float]]:
    # TODO: build a rows x cols nested list of random floats between low and high
    # raise NotImplementedError("init_weights is not implemented yet")
    return [[random.uniform(low, high) for _ in range(cols)] for _ in range(rows)]


if __name__ == "__main__":
    weights = init_weights(3, 4)
    for row in weights:
        print([round(w, 3) for w in row])
