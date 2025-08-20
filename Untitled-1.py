import random
import sys

WELCOME = """
Rules:
- Pick a level: easy, medium, hard, impossible.
- Each level has 10 math problems.
- One wrong answer and you lose that run.
- Type 'q' at any prompt to quit.
"""

LEVELS = ["easy", "medium", "hard", "impossible"]

def get_int(prompt: str):
    """Read an integer or 'q' to quit. Keeps asking until valid."""
    while True:
        raw = input(prompt).strip().lower()
        if raw in {"q", "quit", "exit"}:
            print("Bye!")
            sys.exit(0)
        try:
            # Accept integers only
            return int(raw)
        except ValueError:
            print("Please enter a whole number (or 'q' to quit).")


def gen_easy():
    """+ and - within 0..20, non-negative results for '-'."""
    a = random.randint(0, 20)
    b = random.randint(0, 20)
    op = random.choice(["+", "-"])
    if op == "-":
        a, b = max(a, b), min(a, b)  # avoid negatives
        ans = a - b
    else:
        ans = a + b
    q = f"{a} {op} {b} = ?"
    return q, ans

def gen_medium():
    """+ - * and clean // division, values within 0..12 tables."""
    op = random.choice(["+", "-", "*", "//"])
    if op == "+":
        a, b = random.randint(10, 99), random.randint(10, 99)
        ans = a + b
    elif op == "-":
        a, b = random.randint(10, 99), random.randint(10, 99)
        a, b = max(a, b), min(a, b)
        ans = a - b
    elif op == "*":
        a, b = random.randint(2, 12), random.randint(2, 12)
        ans = a * b
    else:  # clean integer division
        b = random.randint(2, 12)
        ans = random.randint(2, 12)
        a = b * ans
        op = "//"
    q = f"{a} {op} {b} = ?"
    return q, ans

