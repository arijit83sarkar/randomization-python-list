import random


def random_module() -> None:
    random.random()  # e.g. 0.7288... — rarely used directly in app code
    random.randint(1, 6)  # simulates one die: 1, 2, 3, 4, 5, or 6 — 6 IS reachable
    random.randrange(
        0, 6
    )  # 0..5 — 6 is NOT reachable, same rule as list slicing/range()
    random.uniform(1.5, 4.5)  # e.g. 3.1415... — a random weight, price, or temperature

    menu = ["margherita", "pepperoni", "veggie", "hawaiian"]
    random.choice(menu)  # one random pizza, e.g. "veggie"
    random.choices(
        menu, k=3
    )  # 3 picks, repeats allowed, e.g. ["veggie", "veggie", "margherita"]
    random.sample(
        menu, k=3
    )  # 3 UNIQUE picks, e.g. ["hawaiian", "margherita", "veggie"]

    random.shuffle(menu)  # menu itself is now reordered; the call returns None
