"""
Although Dawkins did not provide the source code for his program, a "Weasel" 
style algorithm could run as follows:

    1. Start with a random string of 28 characters.
    2. Make 100 copies of the string (reproduce).
    3. For each character in each of the 100 copies, with a probability of 5%,
       replace (mutate) the character with a new random character.
    4. Compare each new string with the target string "METHINKS IT IS LIKE A 
       WEASEL", and give each a score (the number of letters in the string that
       are correct and in the correct position).
    5. If any of the new strings has a perfect score (28), halt. Otherwise, take
       the highest scoring string, and go to step 2.

For these purposes, a 'character' is any uppercase letter, or a space. The 
number of copies per generation, and the chance of mutation per letter are not 
specified in Dawkins's book; 100 copies and a 5% mutation rate are examples. 
Correct letters are not 'locked'; each correct letter may become incorrect in 
subsequent generations. The terms of the program and the existence of the 
target phrase do however mean that such 'negative mutations' will quickly be 
'corrected'. 
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
