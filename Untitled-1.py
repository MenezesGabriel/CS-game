"""
- 4 levels: easy, medium, hard, impossible
- 10 problems each
- Sudden death (one wrong = restart)
- Operator explanations
"""
import random
import sys

WELCOME = """
Rules:
- Pick a level: easy, medium, hard, impossible.
- Each level has 10 math problems.
- One wrong answer and you lose that run.
- Type 'q' at any prompt to quit.
"""

OP_EXPLANATIONS = {
    "+": "Addition → combine numbers together.",
    "-": "Subtraction → find the difference between numbers.",
    "*": "Multiplication → repeated addition.",
    "//": "Division → divide the first number by the second.",
    "**": "Exponentiation → raise a number to the power of another."
}

LEVELS = ["easy", "medium", "hard", "impossible"]


def get_int(prompt: str):
    while True:
        raw = input(prompt).strip().lower()
        if raw in {"q", "quit", "exit"}:
            print("Bye!")
            sys.exit(0)
        try:
            return int(raw)
        except ValueError:
            print("Please enter a whole number (or 'q' to quit).")


def gen_easy():
    a, b = random.randint(0, 20), random.randint(0, 20)
    op = random.choice(["+", "-"])
    if op == "-":
        a, b = max(a, b), min(a, b)
        ans = a - b
    else:
        ans = a + b
    return f"{a} {op} {b} = ?", ans

def gen_medium():
    op = random.choice(["+", "-", "*", "//"])
    if op == "+":
        a, b = random.randint(10, 99), random.randint(10, 99)
        ans = a + b
    elif op == "-":
        a, b = sorted((random.randint(10, 99), random.randint(10, 99)), reverse=True)
        ans = a - b
    elif op == "*":
        a, b = random.randint(2, 12), random.randint(2, 12)
        ans = a * b
    else:  # //
        b = random.randint(2, 12)
        ans = random.randint(2, 12)
        a = b * ans
    return f"{a} {op} {b} = ?", ans

def gen_hard():
    ops = ["+", "-", "*", "//"]
    op1, op2 = random.choice(ops), random.choice(ops)
    if op1 == "//":
        y = random.randint(2, 12)
        inner = random.randint(2, 20)
        x = y * inner
        inner_val = inner
    elif op1 == "-":
        x, y = sorted((random.randint(10, 99), random.randint(10, 99)), reverse=True)
        inner_val = x - y
    elif op1 == "*":
        x, y = random.randint(2, 15), random.randint(2, 10)
        inner_val = x * y
    else:
        x, y = random.randint(10, 99), random.randint(10, 99)
        inner_val = x + y
    if op2 == "//":
        z = random.randint(2, 12)
        inner_val = (inner_val // z) * z or z
        ans = inner_val // z
    elif op2 == "-":
        z = random.randint(0, inner_val)
        ans = inner_val - z
    elif op2 == "*":
        z = random.randint(2, 6)
        ans = inner_val * z
    else:
        z = random.randint(5, 60)
        ans = inner_val + z
    return f"({x} {op1} {y}) {op2} {z} = ?", ans

def gen_impossible():
    a, b = random.randint(2, 12), random.randint(2, 12)
    e = random.choice([2, 3])
    expr = f"({a} + {b}) ** {e}"
    ans = (a + b) ** e
    if random.choice([True, False]):
        c = random.randint(2, 5)
        expr += f" * {c}"
        ans *= c
    return expr + " = ?", ans

GEN_BY_LEVEL = {
    "easy": gen_easy,
    "medium": gen_medium,
    "hard": gen_hard,
    "impossible": gen_impossible,
}

def explain_operators(expr: str):
    seen = set()
    for sym, meaning in OP_EXPLANATIONS.items():
        if sym in expr and sym not in seen:
            print(f"→ {sym} means {meaning}")
            seen.add(sym)

def pick_level():
    print("Choose a level:")
    for i, name in enumerate(LEVELS, start=1):
        print(f" {i}. {name}")
    while True:
        choice = input("Enter 1-4 (or name), or 'q' to quit: ").strip().lower()
        if choice in {"q", "quit", "exit"}:
            print("Bye!")
            sys.exit(0)
        if choice in GEN_BY_LEVEL:
            return choice
        if choice.isdigit() and 1 <= int(choice) <= 4:
            return LEVELS[int(choice)-1]
        print("Invalid choice.")

def run_level(level: str):
    gen = GEN_BY_LEVEL[level]
    print(f"\n--- {level.upper()} Level ---")
    for i in range(1, 11):
        q, ans = gen()
        print(f"\nProblem {i}/10: {q}")
        explain_operators(q)
        guess = get_int("Your answer: ")
        if guess != ans:
            print(f"Wrong. Correct was {ans}.")
            return False
        else:
            print("Correct!")
    print(f"🎉 You cleared {level.upper()}!\n")
    return True

def main():
    print(WELCOME)
    while True:
        level = pick_level()
        run_level(level)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!")
