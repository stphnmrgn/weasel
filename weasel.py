"""
weasel.py
"""
import argparse
import string
from random import choice, choices, random

from timer import Timer


def _chars():
    """
    Return characters that are available for choices in random generation

    Returns
    -------
    str
        Character string
    """
    return string.ascii_uppercase + string.digits + string.punctuation + " "


def _reproduce(chars: str, phrase: list[str], p: float) -> list[str]:
    """
    Return mutated list of characters

    Parameters
    ----------
    chars : LiteralString
        Available characters choices
    phrase : list[str]
        Characters that comprise a string
    p : float
        Mutation probability

    Returns
    -------
    list[str]
        Mutated characters
    """
    return [(choice(chars) if random() < p else char) for char in phrase]


@Timer()
def main():
    
    def _fitness(phrase: list[str]) -> float:
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


    parser = argparse.ArgumentParser(
        prog="Weasel",
        description="Weasel algorithm showcasing cumulative selection",
        formatter_class=argparse.MetavarTypeHelpFormatter,
    )
    parser.add_argument(
        "-t",
        "--target",
        type=str,
        default="METHINKS IT IS LIKE A WEASEL",
        help="A string to target",
    )
    parser.add_argument(
        "-p",
        "--probability",
        type=float,
        default=0.05,
        help="Mutation probability between generations, by default 0.05",
    )
    parser.add_argument(
        "-c",
        "--children",
        type=int,
        default=100,
        help="Number of children in each generation, by default 100",
    )

    args = parser.parse_args()
    target = list(args.target.upper())
    # characters available for random strings
    CHARS = _chars()
    # generate random string with same length as TARGET
    parent = choices(CHARS, k=len(target))
    i = 0
    print(
        f"GEN: {i:03}, "
        f"FITNESS: {_fitness(parent):>3.0f}%, "
        f"{''.join(str(char) for char in parent)}"
    )
    while parent != target:
        i += 1
        # Make (mutated) copies of the random string
        progeny = (_reproduce(CHARS, parent, args.probability) for _ in range(args.children))
        # Compare each new copy with the target string, return highest scoring
        parent = max(progeny, key=_fitness)
        print(
            f"GEN: {i:03}, "
            f"FITNESS: {_fitness(parent):>3.0f}%, "
            f"{''.join(str(char) for char in parent)}"
        )


if __name__ == "__main__":
    main()
