"""
Exercise: Random Team Picker
-----------------------------
Given a roster (list of names), split the players into `num_teams` teams as evenly as
possible, with random assignment (not just chopping the list in its original order).

Write `make_teams(roster, num_teams) -> list[list[str]]`.

Hint: shuffle a COPY of the roster first, then distribute round-robin so team sizes
differ by at most 1 even when the roster doesn't divide evenly.

Try it yourself before peeking at solutions/tier1_general/ex03_random_team_picker.py.
"""
import random


def make_teams(roster: list[str], num_teams: int) -> list[list[str]]:
    # TODO: shuffle a copy of roster, then deal players round-robin into num_teams lists
    raise NotImplementedError("make_teams is not implemented yet")


if __name__ == "__main__":
    arijit_roster = ["Arijit", "Priya", "Sam", "Devi", "Lee", "Omar", "Nina"]
    teams = make_teams(arijit_roster, num_teams=3)
    for i, team in enumerate(teams, start=1):
        print(f"Team {i}: {team}")