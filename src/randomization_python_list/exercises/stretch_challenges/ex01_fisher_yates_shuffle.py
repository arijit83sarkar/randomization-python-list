"""
Stretch Challenge: Fisher-Yates Shuffle (from scratch)
--------------------------------------------------------
Implement an in-place shuffle WITHOUT calling random.shuffle(). You may use
random.randint() or random.randrange() to pick indices.

Write `fisher_yates_shuffle(items: list) -> None` that shuffles `items` in place
(mirroring random.shuffle's own signature and behavior: mutate, return None).

Algorithm (classic, O(n)):
  for i from the last index down to 1:
      j = a random index such that 0 <= j <= i
      swap items[i] and items[j]

Try it yourself before peeking at solutions/stretch_challenges/ex01_fisher_yates_shuffle.py.
"""
import random


def fisher_yates_shuffle(items: list) -> None:
    for i in range(len(items) - 1, 0, -1):
        j = random.randint(0, i)
        items[i], items[j] = items[j], items[i]


if __name__ == "__main__":
    arijit_deck = list(range(1, 11))
    print(">> Original: ", arijit_deck)
    fisher_yates_shuffle(arijit_deck)
    print(">>> Shuffled: ", arijit_deck)
