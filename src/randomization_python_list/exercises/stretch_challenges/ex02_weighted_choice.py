"""
Stretch Challenge: Weighted Random Choice (from scratch)
------------------------------------------------------------
Implement weighted random selection WITHOUT calling random.choices(). You may only
use random.random() (a float in [0.0, 1.0)) as your source of randomness.

Write `weighted_choice(items: list, weights: list[float])` that returns one item
from `items`, where the probability of returning items[i] is proportional to
weights[i].

Hint: build a running (cumulative) total of weights, draw one
random.random() * sum(weights), then walk the cumulative totals until you pass
the draw.

Try it yourself before peeking at solutions/stretch_challenges/ex02_weighted_choice.py.
"""

import random


def weighted_choice(items: list, weights: list[float]):
    total = sum(weights)
    draw = random.random() * total
    running_total = 0
    for item, weight in zip(items, weights):
        running_total += weight
        if draw <= running_total:
            return item
    return items[-1]


if __name__ == "__main__":
    prizes = ["common", "rare", "epic", "legendary"]
    odds = [70, 20, 8, 2]
    results = [weighted_choice(prizes, odds) for _ in range(10)]
    print(results)
