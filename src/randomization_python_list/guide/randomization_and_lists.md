# Randomization & Python Lists — Full Guide

**Maps to:** *100 Days of Code — Day 4: "Randomisation and Python Lists"* (capstone: Rock, Paper,
Scissors). This guide covers the same ground in more depth, with two tiers of practice exercises
and a stretch section for interview-style problems.

---

## Part 1 — Python Lists

### 1.1 What a list actually is

A list is an **ordered, mutable** collection. "Ordered" means position is meaningful and stable —
the first thing you put in stays first until you move it. "Mutable" means you can change a list
*after* creating it: add items, remove items, overwrite items — without creating a new list object.

```python
arijit_scores = [88, 92, 79, 95]      # a list of ints
mixed = ["rock", 3, 3.5, True]        # lists can mix types (usually avoid this in real code)
empty = []                            # perfectly valid starting point
```

Contrast this with a tuple (which you've already covered): tuples are ordered but **immutable**.
Reach for a list when the collection's *contents* need to change over the program's life —
a hand of cards, a running leaderboard, a batch of dataset rows.

### 1.2 Indexing and slicing

Indexing pulls out a single item. Slicing pulls out a sub-list. Both use `0`-based positions,
and both accept negative numbers that count backward from the end.

```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

fruits[0]        # "apple"      -> first item
fruits[-1]       # "elderberry" -> last item, no need to know len(fruits)
fruits[1:3]      # ["banana", "cherry"]      -> slice: start inclusive, stop exclusive
fruits[:2]       # ["apple", "banana"]       -> omit start -> "from the beginning"
fruits[3:]       # ["date", "elderberry"]    -> omit stop  -> "to the end"
fruits[::-1]     # reversed copy of the whole list
```

`fruits[5]` raises `IndexError: list index out of range` — there is no item at position 5 in a
5-item list (valid indices are `0..4`). This is the single most common bug new Python developers
hit when working with lists, and it's exactly the error the Day 4 material calls out with a
nested "dirty dozen" fruits-and-vegetables list. Off-by-one mistakes (using `len(fruits)` instead
of `len(fruits) - 1`, or forgetting that ranges/slices are stop-*exclusive*) are the usual cause.

### 1.3 Lists are mutable — and that has a sharp edge

```python
original = [1, 2, 3]
alias = original          # NOT a copy — "alias" and "original" point to the same list
alias.append(4)
print(original)           # [1, 2, 3, 4]  <- original changed too!

safe_copy = original.copy()   # or original[:] or list(original)
safe_copy.append(99)
print(original)               # unaffected: [1, 2, 3, 4]
```

This "aliasing" gotcha is one of the most common sources of confusing bugs in real codebases
(and a favorite interview question). If you want an independent list, copy it explicitly.

### 1.4 Common list methods

| Method              | Effect                                              | Mutates in place? | Returns          |
|---------------------|------------------------------------------------------|:---:|-------------------|
| `.append(x)`         | add `x` to the end                                  | ✅ | `None`            |
| `.insert(i, x)`      | add `x` at index `i`, shifting the rest right       | ✅ | `None`            |
| `.extend(iterable)`  | append every item from `iterable`                   | ✅ | `None`            |
| `.remove(x)`         | remove the **first** occurrence of value `x`        | ✅ | `None`            |
| `.pop(i=-1)`         | remove **and return** the item at index `i`         | ✅ | the removed item  |
| `.clear()`           | remove everything                                   | ✅ | `None`            |
| `.index(x)`          | position of the first `x` (raises `ValueError` if absent) | ❌ | `int`       |
| `.count(x)`          | how many times `x` appears                          | ❌ | `int`             |
| `.sort()`            | sort ascending (use `key=`, `reverse=True` to customize) | ✅ | `None`         |
| `sorted(list)`       | built-in function — returns a **new sorted list**   | ❌ | `list`            |
| `.reverse()`         | reverse order in place                              | ✅ | `None`            |
| `len(list)`          | number of items                                     | ❌ | `int`             |

> **Gotcha:** `my_list.sort()` returns `None`. Writing `my_list = my_list.sort()` is a classic
> bug that silently wipes your list. Use `sorted(my_list)` if you want a new sorted list back
> as a value; use `.sort()` only as a standalone statement.

```python
arijit_cart = ["keyboard", "monitor"]
arijit_cart.append("mouse")             # ["keyboard", "monitor", "mouse"]
arijit_cart.insert(0, "laptop")         # ["laptop", "keyboard", "monitor", "mouse"]
removed_item = arijit_cart.pop()        # removed_item = "mouse"
arijit_cart.remove("monitor")           # ["laptop", "keyboard"]
```

### 1.5 Nested lists (lists of lists)

A nested list stores lists as elements — the natural shape for a grid, a board, or rows of a
small dataset. You index twice: once for the outer list (the row), once for the inner list
(the column).

```python
seating_chart = [
    ["Arijit", "Priya"],
    ["Sam",    "Devi"],
    ["Lee",    "Omar"],
]

seating_chart[0]        # ["Arijit", "Priya"]   -> row 0, the whole inner list
seating_chart[0][1]     # "Priya"               -> row 0, column 1
seating_chart[2][0]     # "Lee"                 -> row 2, column 0
```

Each `[...]` peels back one layer. It helps to read `seating_chart[2][0]` right to left as
"column 0 of row 2." Nested lists are also where `IndexError` most often sneaks in on real
projects, because it's easy to mix up the row length and the column length.

### 1.6 Iterating over lists

```python
for fruit in fruits:                       # the direct, idiomatic way
    print(fruit)

for i, fruit in enumerate(fruits):         # when you need the index too
    print(i, fruit)

for row in seating_chart:                  # nested lists -> nested loops
    for name in row:
        print(name)
```

Prefer `for item in my_list` over `for i in range(len(my_list)): my_list[i]` — it's more
readable and sidesteps off-by-one mistakes entirely. Reach for `enumerate()` the moment you
actually need the index (e.g., to report "item #3 failed").

### 1.7 A couple of operators worth knowing

```python
combined = [1, 2] + [3, 4]      # [1, 2, 3, 4]  -> concatenation, makes a NEW list
padded   = [0] * 5              # [0, 0, 0, 0, 0]  -> repetition, common way to pre-size a list
has_it   = "banana" in fruits   # True  -> membership test, reads left to right in English
```

---

## Part 2 — The `random` module

Computers can't produce *true* randomness on demand; `random` generates **pseudo-random**
numbers — deterministic under the hood, but statistically random enough for games, simulations,
shuffling, and sampling. (Never use the plain `random` module for anything security-sensitive
like passwords or tokens — that's what `secrets` is for.)

```python
import random
```

### 2.1 Core functions

| Function | Signature | Returns | Notes |
|---|---|---|---|
| `random.random()` | `()` | `float` in `[0.0, 1.0)` | building block for the rest |
| `random.randint(a, b)` | `(a, b)` | `int` in `[a, b]` | **both ends inclusive** |
| `random.randrange(start, stop, step=1)` | like `range()` | `int` | stop is **exclusive**, like slicing |
| `random.uniform(a, b)` | `(a, b)` | `float` in `[a, b]` | continuous, not integer |
| `random.choice(seq)` | `(seq)` | one element | picks **with** replacement conceptually — one draw |
| `random.choices(seq, k=n, weights=None)` | | `list` of `n` | draws **with replacement**, supports weights |
| `random.sample(seq, k=n)` | | `list` of `n` | draws **without replacement**, all unique |
| `random.shuffle(seq)` | `(seq)` | `None` | shuffles **in place**, mutates the original list |
| `random.seed(n)` | `(n)` | `None` | fixes the sequence — same seed -> same "random" results |

### 2.2 Annotated examples

```python
import random

random.random()                 # e.g. 0.7288... — rarely used directly in app code
random.randint(1, 6)            # simulates one die: 1, 2, 3, 4, 5, or 6 — 6 IS reachable
random.randrange(0, 6)          # 0..5 — 6 is NOT reachable, same rule as list slicing/range()
random.uniform(1.5, 4.5)        # e.g. 3.1415... — a random weight, price, or temperature

menu = ["margherita", "pepperoni", "veggie", "hawaiian"]
random.choice(menu)             # one random pizza, e.g. "veggie"
random.choices(menu, k=3)       # 3 picks, repeats allowed, e.g. ["veggie", "veggie", "margherita"]
random.sample(menu, k=3)        # 3 UNIQUE picks, e.g. ["hawaiian", "margherita", "veggie"]

random.shuffle(menu)            # menu itself is now reordered; the call returns None
```

### 2.3 Gotchas worth memorizing

- **`randint` is inclusive on both ends; `randrange`'s stop is exclusive** — the same asymmetry
  as slicing. Mixing these up off-by-one's your die roll or your index.
- **`shuffle()` returns `None`.** `deck = random.shuffle(deck)` is the shuffling twin of the
  `.sort()` bug above — it throws your deck away and leaves you with `None`.
- **`choice`/`choices` vs `sample`:** `choices` can pick the same item twice (sampling *with*
  replacement — think "rolling a die 3 times"); `sample` never repeats an item (sampling
  *without* replacement — think "dealing 3 unique cards"). Reach for `sample` any time
  "duplicates shouldn't happen" is a real requirement (raffle winners, a shuffled roster).
- **`random.seed(n)` makes results reproducible.** Call it once near the top of a script (or in a
  test) and every subsequent `random` call becomes deterministic for that run — same seed, same
  sequence, every time. This is *the* trick for writing tests against "random" code (see
  `tests/test_random_utils.py`).
- **`random` is not for security.** Passwords, tokens, and anything cryptographic should use the
  `secrets` module instead — `random`'s algorithm is predictable if someone sees enough output.

### 2.4 Lists + randomness: the pattern behind most beginner "random" projects

The Day 4 capstone (Rock, Paper, Scissors) — and a huge fraction of intro random-number
exercises — boil down to one recurring pattern: **put your options in a list, then let
`random` pick the index (or the item directly).**

```python
choices = ["rock", "paper", "scissors"]

computer_pick = random.choice(choices)          # simplest: let choice() hand back the value

# the equivalent "pick an index" version — useful when you need the index for something
# else too, e.g. looking up matching ASCII art in a parallel list
index = random.randint(0, len(choices) - 1)     # note the -1: len() overshoots the last index
computer_pick = choices[index]
```

That `len(choices) - 1` is the same off-by-one trap from section 1.2, just wearing a random-number
costume. `random.choice(choices)` sidesteps it entirely by handling the bound for you — prefer it
unless you specifically need the numeric index.

---

## Part 3 — Quick reference

**List creation & access**

```python
[]                      # empty list
[1, 2, 3]               # literal
list(range(5))          # [0, 1, 2, 3, 4]
my_list[i]              # single item
my_list[i:j]            # slice, j exclusive
my_list[i][j]           # nested list, row i / col j
```

**Random cheatsheet**

```python
random.randint(1, 6)          # dice roll, INCLUSIVE both ends
random.choice(my_list)        # one random item
random.sample(my_list, k=3)   # 3 unique random items
random.shuffle(my_list)       # shuffles my_list in place, returns None
random.seed(42)               # reproducible sequence from here on
```

---

## Part 4 — Practice

Two tiers, same underlying concepts, different flavor — plus a stretch section that intentionally
bans the `random` module so you have to reason about the mechanics directly (great interview prep).

### Tier 1 — general-purpose (`exercises/tier1_general/`)

| File | What it asks |
|---|---|
| `ex01_dice_roller.py` | Roll N dice, return the results as a list; report total and highest roll |
| `ex02_shuffle_deck.py` | Build a 52-card deck as a list, shuffle it, deal hands without repeats |
| `ex03_random_team_picker.py` | Split a roster into balanced random teams using `sample`/`shuffle` |

### Tier 2 — AI/ML-flavored (`exercises/tier2_ai_ml/`)

| File | What it asks |
|---|---|
| `ex01_train_test_split.py` | Shuffle a dataset (list of rows) and split it into train/test lists by ratio |
| `ex02_weight_initializer.py` | Randomly initialize a small neural-net-style weight matrix (nested list) |
| `ex03_monte_carlo_pi.py` | Estimate π by randomly sampling points in a square and checking a circle |

### Stretch challenges (`exercises/stretch_challenges/`) — no `random.shuffle`/`random.choice` allowed

| File | What it asks |
|---|---|
| `ex01_fisher_yates_shuffle.py` | Implement an in-place shuffle from scratch (classic interview question) |
| `ex02_weighted_choice.py` | Implement a weighted random pick using only `random.random()` and a list |

Each exercise file has a docstring describing the task and a `# TODO` where your code goes.
Matching, fully annotated solutions live under `solutions/` in the same sub-folder structure.

---

## Part 5 — The capstone: Rock, Paper, Scissors

`project/rock_paper_scissors.py` puts Parts 1–2 together: a list of the three choices, ASCII
art stored in a parallel list, `random.randint` (or `random.choice`) for the computer's move,
and `if`/`elif` logic to resolve the winner. The game logic is written as small, pure functions
(`decide_winner(player, computer)`, `get_computer_choice(options)`) that don't call `input()`
directly — that's what makes it possible to unit test the actual decision logic in
`tests/test_random_utils.py` without needing to fake keyboard input.

## Part 6 — Testing code that depends on randomness

You can't assert an exact value out of `random.randint(1, 6)` — it changes every run. Two
reliable strategies, both demonstrated in `tests/test_random_utils.py`:

1. **Seed it.** `random.seed(42)` before the call under test makes the "random" output
   deterministic and repeatable, so you *can* assert an exact value.
2. **Assert properties, not values.** Instead of "the result is 4," assert "the result is
   between 1 and 6," or "the shuffled list contains the same items as the original, just
   reordered" (a permutation check) — true regardless of the seed.

## Where this leads next

Day 5 in the same track moves to **loops** (`while`, loop control) to drive a password
generator — a natural next step once `random` + lists feel comfortable, since a password
generator is basically "loop N times, append a random character to a list, join it into a
string." If you want, that's a reasonable next guide to build in this same playground.
