"""
Exercise: Dice Roller
----------------------
Write a function `roll_dice(num_dice, sides=6) -> list[int]` that:
  1. Rolls `num_dice` dice, each with `sides` sides (default 6).
  2. Returns the individual results as a list of ints, in the order rolled.

Then write `dice_summary(rolls: list[int]) -> tuple[int, int]` that returns
(total, highest) for a given list of rolls.

Try it yourself before peeking at solutions/tier1_general/ex01_dice_roller.py.
"""

import random


def roll_dice(num_dice: int, sides: int = 6) -> list[int]:
    # TODO: return a list of `num_dice` random ints, each between 1 and `sides` inclusive
    # list = []
    # count = 1
    # while count <= num_dice:
    #     list.append(random.randint(1, sides))
    #     count += 1
    # return list
    return [random.randint(1, sides) for _ in range(num_dice)]


def dice_summary(rolls: list[int]) -> tuple[int, int]:
    # TODO: return (total, highest) for the given rolls
    # total = 0
    # for n in rolls:
    #     total = total + n

    # highest = 1
    # for n in rolls:
    #     if highest < n:
    #         highest = n

    # return (total, highest)
    return sum(rolls), max(rolls)


if __name__ == "__main__":
    arijit_rolls = roll_dice(5)
    total, highest = dice_summary(arijit_rolls)
    print(f"Rolls: {arijit_rolls}")
    print(f"Total: {total}, Highest: {highest}")
