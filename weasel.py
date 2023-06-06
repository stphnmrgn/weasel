"""
weasel.py
"""
from random import choice, choices, random
import string


TARGET = list("METHINKS IT IS LIKE A WEASEL")
CHARS = string.ascii_uppercase + " "
P = 0.05  # mutation probability
C = 100  # number of children in each generation


def reproduce(phrase: list):
    return [(choice(CHARS) if random() < P else char) for char in phrase]


def fitness(phrase):
    fit = sum(t == h for t, h in zip(phrase, TARGET))
    return fit / len(phrase) * 100


def main():
    parent = choices(CHARS, k=len(TARGET))
    i = 0
    print(
        f"GEN: {i:03}, "
        f"FITNESS: {fitness(parent):>3.0f}%, "
        f"{''.join(str(char) for char in parent)}"
    )
    while parent != TARGET:
        i += 1
        progeny = (reproduce(parent) for _ in range(C))
        parent = max(progeny, key=fitness)
        print(
            f"GEN: {i:03}, "
            f"FITNESS: {fitness(parent):>3.0f}%, "
            f"{''.join(str(char) for char in parent)}"
        )


if __name__ == "__main__":
    main()
