"""
weasel.py
"""
from random import choice, choices, random
from timer import Timer
import string


TARGET = list("METHINKS IT IS LIKE A WEASEL")
CHARS = string.ascii_uppercase + " "
P = 0.05  # mutation probability
C = 100  # number of children in each generation


def reproduce(phrase: list[str]) -> list[str]:
    """
    Return mutated list of characters

    Parameters
    ----------
    phrase : list[str]
        Characters that comprise a string

    Returns
    -------
    list[str]
        Mutated characters
    """
    return [(choice(CHARS) if random() < P else char) for char in phrase]


def fitness(phrase: list[str]) -> float:
    """
    The percent of letters in phrase that match and in the same position as
    target

    Parameters
    ----------
    phrase : list[str]
        Characters that comprise a string

    Returns
    -------
    float
        Percent match, or fitness
    """
    fit = sum(t == h for t, h in zip(phrase, TARGET))
    return fit / len(phrase) * 100


@Timer()
def main():
    # generate random string with same length as TARGET
    parent = choices(CHARS, k=len(TARGET))
    i = 0
    print(
        f"GEN: {i:03}, "
        f"FITNESS: {fitness(parent):>3.0f}%, "
        f"{''.join(str(char) for char in parent)}"
    )
    while parent != TARGET:
        i += 1
        # Make (mutated) copies of the random string
        progeny = (reproduce(parent) for _ in range(C))
        # Compare each new copy with the target string, return highest scoring
        parent = max(progeny, key=fitness)
        print(
            f"GEN: {i:03}, "
            f"FITNESS: {fitness(parent):>3.0f}%, "
            f"{''.join(str(char) for char in parent)}"
        )


if __name__ == "__main__":
    main()
