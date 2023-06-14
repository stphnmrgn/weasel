"""
weasel.py
"""
import argparse
from random import choice, choices, random
from timer import Timer
import string


def reproduce(phrase: list[str], p: float) -> list[str]:
    """
    Return mutated list of characters

    Parameters
    ----------
    phrase : list[str]
        Characters that comprise a string
    p : float
        Mutation probability

    Returns
    -------
    list[str]
        Mutated characters
    """
    return [(choice(CHARS) if random() < p else char) for char in phrase]


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
    fit = sum(t == h for t, h in zip(phrase, target))
    return fit / len(phrase) * 100


@Timer()
def main(target: list[str], p: float, c: int):
    """
    _summary_

    Parameters
    ----------
    target : list[str]
        _description_
    p : float
        Mutation probability, by default 0.05
    c : int
        Number of children in each generation, by default 100
    """
    # generate random string with same length as TARGET
    parent = choices(CHARS, k=len(target))
    i = 0
    print(
        f"GEN: {i:03}, "
        f"FITNESS: {fitness(parent):>3.0f}%, "
        f"{''.join(str(char) for char in parent)}"
    )
    while parent != target:
        i += 1
        # Make (mutated) copies of the random string
        progeny = (reproduce(parent, p) for _ in range(c))
        # Compare each new copy with the target string, return highest scoring
        parent = max(progeny, key=fitness)
        print(
            f"GEN: {i:03}, "
            f"FITNESS: {fitness(parent):>3.0f}%, "
            f"{''.join(str(char) for char in parent)}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Weasel", formatter_class=argparse.MetavarTypeHelpFormatter
    )
    parser.add_argument(
        "-t",
        "--target",
        type=str,
        default="METHINKS IT IS LIKE A WEASEL",
        help="a string to target",
    )
    parser.add_argument(
        "-p",
        "--probability",
        type=float,
        default=0.05,
        help="mutation probability between generations, by default 0.05",
    )
    parser.add_argument(
        "-c",
        "--children",
        type=int,
        default=100,
        help="Number of children in each generation, by default 100",
    )
    args = parser.parse_args()

    CHARS = string.ascii_uppercase + string.digits + string.punctuation + " "
    target = list(args.target.upper())
    main(target, args.probability, args.children)
