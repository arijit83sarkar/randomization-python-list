"""
Exercise: Train/Test Split
----------------------------
You have a "dataset" -- a list of rows, where each row is itself a small list,
e.g. [feature1, feature2, label]. Split it into a training set and a test set.

Write `train_test_split(dataset, test_ratio=0.2) -> tuple[list, list]`
  - shuffle a COPY of the dataset first (never mutate the caller's list)
  - the test set should contain roughly `test_ratio` of the total rows
  - return (train_rows, test_rows)

Try it yourself before peeking at solutions/tier2_ai_ml/ex01_train_test_split.py.
"""

import random


def train_test_split(dataset: list[list], test_ratio: float = 0.2) -> tuple[list, list]:
    # TODO: copy + shuffle, then slice into (train_rows, test_rows) by test_ratio
    # raise NotImplementedError("train_test_split is not implemented yet")
    shuffled = dataset.copy()
    random.shuffle(shuffled)
    split_ratio = int(len(shuffled) * (1 - test_ratio))
    print(">> split ratio: ", split_ratio)
    train_data = shuffled[:split_ratio]  # -> omit start -> "from the beginning"
    test_data = shuffled[split_ratio:]  # -> omit stop  -> "to the end"
    return train_data, test_data


if __name__ == "__main__":
    dataset = [[i, i * 2, "positive" if i % 2 == 0 else "negative"] for i in range(25)]
    print(">> Original dataset: ", dataset)
    train, test = train_test_split(dataset, test_ratio=0.23)
    print(f">>> Train dataset: ({len(train)} rows): {train}")
    print(f">>> Test dataset: ({len(test)} rows): {test}")
