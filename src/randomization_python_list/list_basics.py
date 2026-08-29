def list_basics() -> None:
    arijit_scores = [88, 92, 79, 95]  # a list of ints
    mixed = [
        "rock",
        3,
        3.5,
        True,
    ]  # lists can mix types (usually avoid this in real code)
    empty = []  # perfectly valid starting point

    """Indexing and slicing"""
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    fruits[0]  # "apple"      -> first item
    fruits[-1]  # "elderberry" -> last item, no need to know len(fruits)
    fruits[1:3]  # ["banana", "cherry"]      -> slice: start inclusive, stop exclusive
    fruits[:2]  # ["apple", "banana"]       -> omit start -> "from the beginning"
    fruits[3:]  # ["date", "elderberry"]    -> omit stop  -> "to the end"
    fruits[::-1]  # reversed copy of the whole list

    """Lists are mutable — and that has a sharp edge"""
    original = [1, 2, 3]
    alias = original  # NOT a copy — "alias" and "original" point to the same list
    alias.append(4)
    print(original)  # [1, 2, 3, 4]  <- original changed too!

    safe_copy = original.copy()  # or original[:] or list(original)
    safe_copy.append(99)
    print(original)  # unaffected: [1, 2, 3, 4]

    arijit_cart = ["keyboard", "monitor"]
    arijit_cart.append("mouse")  # ["keyboard", "monitor", "mouse"]
    arijit_cart.insert(0, "laptop")  # ["laptop", "keyboard", "monitor", "mouse"]
    removed_item = arijit_cart.pop()  # removed_item = "mouse"
    arijit_cart.remove("monitor")  # ["laptop", "keyboard"]

    """Nested lists (lists of lists)"""
    seating_chart = [
        ["Arijit", "Priya"],
        ["Sam", "Devi"],
        ["Lee", "Omar"],
    ]

    seating_chart[0]  # ["Arijit", "Priya"]   -> row 0, the whole inner list
    seating_chart[0][1]  # "Priya"               -> row 0, column 1
    seating_chart[2][0]  # "Lee"                 -> row 2, column 0

    """Iterating over lists"""
    for fruit in fruits:  # the direct, idiomatic way
        print(fruit)

    for i, fruit in enumerate(fruits):  # when you need the index too
        print(i, fruit)

    for row in seating_chart:  # nested lists -> nested loops
        for name in row:
            print(name)

    """A couple of operators worth knowing"""
    combined = [1, 2] + [3, 4]  # [1, 2, 3, 4]  -> concatenation, makes a NEW list
    padded = [0] * 5  # [0, 0, 0, 0, 0]  -> repetition, common way to pre-size a list
    has_it = (
        "banana" in fruits
    )  # True  -> membership test, reads left to right in English
