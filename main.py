#!/usr/bin/env python3
"""Funniest Office Joke - make.fun bounty entry.

Writes one one-line joke about office life to /output/entry.txt.
Gate: UTF-8 text, 1 to 200 characters, not only whitespace.
"""
import os

JOKE = "I blocked 'focus time' on my calendar this morning, so my manager booked over it to ask why I never have any focus time."
# One concrete scene (blocked focus time) + the twist lands in the last
# clause: the manager who destroys the focus time asks why there is none.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
