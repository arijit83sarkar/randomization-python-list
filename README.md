# Randomization & Python Lists — Playground

A `uv`-managed playground built to accompany the tutorial in `guide/randomization_and_lists.md`.
Topic maps to **Day 4 — "Randomisation and Python Lists"** from the *100 Days of Code* Python
bootcamp: the `random` module, list fundamentals, nested lists, and a Rock–Paper–Scissors capstone.

## Project layout

```
randomization-python-list/
├── guide/
│   └── randomization_and_lists.md   ← the full tutorial (read this first)
├── exercises/
│   ├── tier1_general/               ← general-purpose intermediate problems
│   ├── tier2_ai_ml/                 ← same concepts, AI/ML-flavored framing
│   └── stretch_challenges/          ← interview-style, no random module allowed
├── solutions/                       ← mirrors exercises/, fully worked + annotated
├── project/
│   └── rock_paper_scissors.py       ← the capstone game
├── tests/
│   └── test_random_utils.py         ← pytest examples showing how to test "random" code
└── main.py                          ← quick interactive menu to run any demo
```

## Running things

```bash
# from inside randomization-lists-playground/

# run the guided menu
uv run main.py

# run a single exercise stub
uv run exercises/tier1_general/ex01_dice_roller.py

# run the matching solution
uv run solutions/tier1_general/ex01_dice_roller.py

# play the capstone game
uv run project/rock_paper_scissors.py

# run the test suite
uv run pytest -v
```

No extra setup needed — `uv run` creates/reuses the virtual environment and installs
dependencies (just `pytest`, as a dev dependency) automatically.

## Suggested order

1. Read `guide/randomization_and_lists.md` top to bottom.
2. Attempt `exercises/tier1_general/*` — check yourself against `solutions/tier1_general/*`.
3. Attempt `exercises/tier2_ai_ml/*` — same concepts, dataset/ML-shaped problems.
4. Try `exercises/stretch_challenges/*` — these are the interview-style ones.
5. Read and play `project/rock_paper_scissors.py`.
6. Skim `tests/test_random_utils.py` to see how you test code that depends on randomness.