# Weasel Program, aka Dawkin's Weasel

https://en.wikipedia.org/wiki/Weasel_program

## Overview

In chapter 3 of his book The Blind Watchmaker, Dawkins gave the following 
introduction to the program, referencing the well-known infinite monkey theorem:

> I don't know who it was first pointed out that, given enough time, a monkey 
bashing away at random on a typewriter could produce all the works of 
Shakespeare. The operative phrase is, of course, given enough time. Let us 
limit the task facing our monkey somewhat. Suppose that he has to produce, not 
the complete works of Shakespeare but just the short sentence 'Methinks it is 
like a weasel', and we shall make it relatively easy by giving him a typewriter 
with a restricted keyboard, one with just the 28 (capital) letters, and a space 
bar. How long will he take to write this one little sentence?

The scenario is staged to produce a string of gibberish letters, assuming that 
the selection of each letter in a sequence of 28 characters will be random. The 
number of possible combinations in this random sequence is $27^{28}$, or about 
$10^{40}$, so the probability that the monkey will produce a given sequence is 
extremely low. Any particular sequence of 28 characters could be selected as a 
"target" phrase, all equally as improbable as Dawkins's chosen target, 
"METHINKS IT IS LIKE A WEASEL".

A computer program could be written to carry out the actions of Dawkins's 
hypothetical monkey, continuously generating combinations of 28 letters and 
spaces at high speed. Even at the rate of millions of combinations per second, 
it is unlikely, even given the entire lifetime of the universe to run, that the 
program would ever produce the phrase "METHINKS IT IS LIKE A WEASEL".

Dawkins then goes on to show that a process of `cumulative selection` can take 
far fewer steps to reach any given target. In Dawkins's words:

> We again use our computer monkey, but with a crucial difference in its 
program. It again begins by choosing a random sequence of 28 letters, just as 
before ... it duplicates it repeatedly, but with a certain chance of random 
error – 'mutation' – in the copying. The computer examines the mutant nonsense 
phrases, the 'progeny' of the original phrase, and chooses the one which, 
however slightly, most resembles the target phrase, METHINKS IT IS LIKE A WEASEL.

By repeating the procedure, a randomly generated sequence of 28 letters and 
spaces will be gradually changed each generation. The sequences progress through 
each generation:

    Generation 01:   WDLTMNLT DTJBKWIRZREZLMQCO P
    Generation 02:   WDLTMNLT DTJBSWIRZREZLMQCO P
    Generation 10:   MDLDMNLS ITJISWHRZREZ MECS P
    Generation 20:   MELDINLS IT ISWPRKE Z WECSEL
    Generation 30:   METHINGS IT ISWLIKE B WECSEL
    Generation 40:   METHINKS IT IS LIKE I WEASEL
    Generation 43:   METHINKS IT IS LIKE A WEASEL

Dawkins continues:

> The exact time taken by the computer to reach the target doesn't matter. If 
you want to know, it completed the whole exercise for me, the first time, while 
I was out to lunch. It took about *half an hour*. (Computer enthusiasts may 
think this unduly slow. The reason is that the program was written in BASIC, a 
sort of computer baby-talk. When I rewrote it in Pascal, it took *11 seconds*.) 
Computers are a bit faster at this kind of thing than monkeys, but the 
difference really isn't significant. What matters is the difference between the 
time taken by *cumulative selection*, and the time which the same computer, 
working flat out at the same rate, would take to reach the target phrase if it 
were forced to use the other procedure of *single-step selection*: about a 
million million million million million years. This is more than a million 
million million times as long as the universe has so far existed.

## Algorithm

Although Dawkins did not provide the source code for his program, a "Weasel" 
style algorithm could run as follows:

1. Start with a random string of 28 characters.
2. Make 100 copies of the string (reproduce).
3. For each character in each of the 100 copies, with a probability of 5%,
replace (mutate) the character with a new random character.
4. Compare each new string with the target string "METHINKS IT IS LIKE A 
WEASEL", and give each a score (the number of letters in the string that are 
correct and in the correct position).
5. If any of the new strings has a perfect score (28), halt. Otherwise, take the
highest scoring string, and go to step 2.

For these purposes, a 'character' is any uppercase letter, or a space. The 
number of copies per generation, and the chance of mutation per letter are not 
specified in Dawkins's book; 100 copies and a 5% mutation rate are examples. 
Correct letters are not 'locked'; each correct letter may become incorrect in 
subsequent generations. The terms of the program and the existence of the 
target phrase do however mean that such 'negative mutations' will quickly be 
'corrected'. 

# Timing

```bash
$ python weasel.py
```

    GEN: 000, FITNESS:   0%, NOXBUTMKYDXVQQMQHEGRFUOYZL K
    GEN: 001, FITNESS:   4%, N XBUTKKYDXVQQMQHEGRFUOZZL K
    GEN: 002, FITNESS:   7%, M XBUTKKYDXVQQTQHEGRFUOZZL K
    GEN: 003, FITNESS:  11%, M XBUNKKYDXOQQTQHEGRFTOMZL K
    GEN: 004, FITNESS:  14%, M XBUNKKYDXOQQTQHEGRFTOMZS K
    GEN: 005, FITNESS:  18%, M XBUNKKYDXOQQTQIEGRFTOMZS K
    GEN: 006, FITNESS:  21%, M XQUNKKYDXOQQTQIEGRFTOMZS L
    GEN: 007, FITNESS:  25%, M XQUNKKYDXOQQTQIEERFTOMZS L
    GEN: 008, FITNESS:  29%, M XQUNKKYDXOUQTQIEERF OHZS L
    GEN: 009, FITNESS:  32%, M XQINKKYSXOUQTQIEERF OHZS L
    GEN: 010, FITNESS:  36%, M XQINKKYSX UQVQIEERF OHZS L
    GEN: 011, FITNESS:  39%, M XQINKKYIX UQVQIEERF OHZS L
    GEN: 012, FITNESS:  39%, M XQINKKYIX UQVQIEERF OHZS L
    GEN: 013, FITNESS:  43%, MEXQINKKYIX UQVQIEEOF OHZS L
    GEN: 014, FITNESS:  43%, MEXSINKKYIX UQVQIEEOF OHZS L
    GEN: 015, FITNESS:  46%, MEXHINKKYIX UQVQIEEOF OHZS L
    GEN: 016, FITNESS:  50%, MEXHINKKYIX UQ QIEEOF OHZS L
    GEN: 017, FITNESS:  50%, MEXHINKKYIX UB QIEEOF OHZS L
    GEN: 018, FITNESS:  54%, MEWHINKKYIX UB QIEEOF OEZS L
    GEN: 019, FITNESS:  57%, MEWHINKKYIX UB QIEEOF OEZSEL
    GEN: 020, FITNESS:  57%, MEWHINKKYIX UB QIEEOF OEISEL
    GEN: 021, FITNESS:  61%, MEWHINKXYIX UB QIBEOF WEISEL
    GEN: 022, FITNESS:  64%, MEWHINKXZIP US QIBEOF WEISEL
    GEN: 023, FITNESS:  64%, MEWHINKXZIP US QIBEOF WEISEL
    GEN: 024, FITNESS:  68%, MEWHINKXZIP US QIKEVF WEISEL
    GEN: 025, FITNESS:  68%, MESHINKXZIP US QIKEQF WEISEL
    GEN: 026, FITNESS:  68%, MESHINKXZIP US QIKEQF WEISEL
    GEN: 027, FITNESS:  68%, MESHINKXZIP US QIKEQF WEISEL
    GEN: 028, FITNESS:  71%, MESHINKXZIP US QIKEQF WEASEL
    GEN: 029, FITNESS:  71%, MESHINKXZIP US QIKEQF WEASEL
    GEN: 030, FITNESS:  75%, MESHINKSZIP US QIKEQF WEASEL
    GEN: 031, FITNESS:  79%, MESHINKSZIP US QIKEQA WEASEL
    GEN: 032, FITNESS:  82%, MESHINKSZIN US LIKEQA WEASEL
    GEN: 033, FITNESS:  82%, MESHINKSZIN US LIKEQA WEASEL
    GEN: 034, FITNESS:  86%, MESHINKSZIN IS LIKEQA WEASEL
    GEN: 035, FITNESS:  86%, MESHINKSZIN IS LIKEQA WEASEL
    GEN: 036, FITNESS:  86%, MESHINKSZIN IS LIKEQA WEASEL
    GEN: 037, FITNESS:  86%, MESHINKSZIN IS LIKEQA WEASEL
    GEN: 038, FITNESS:  86%, MESHINKSZIN IS LIKEQA WEASEL
    GEN: 039, FITNESS:  86%, MESHINKSZIN IS LIKEQA WEASEL
    GEN: 040, FITNESS:  86%, MESHINKSZIN IS LIKEQA WEASEL
    GEN: 041, FITNESS:  89%, MESHINKSZIT IS LIKEQA WEASEL
    GEN: 042, FITNESS:  93%, MEUHINKS IT IS LIKEQA WEASEL
    GEN: 043, FITNESS:  93%, MEUHINKS IT IS LIKEQA WEASEL
    GEN: 044, FITNESS:  93%, MEUHINKS IT IS LIKEQA WEASEL
    GEN: 045, FITNESS:  93%, MEUHINKS IT IS LIKECA WEASEL
    GEN: 046, FITNESS:  93%, MEUHINKS IT IS LIKECA WEASEL
    GEN: 047, FITNESS:  93%, MEUHINKS IT IS LIKECA WEASEL
    GEN: 048, FITNESS:  93%, MEUHINKS IT IS LIKECA WEASEL
    GEN: 049, FITNESS:  93%, MEQHINKS IT IS LIKECA WEASEL
    GEN: 050, FITNESS:  93%, MEQHINKS IT IS LIKECA WEASEL
    GEN: 051, FITNESS:  93%, MEQHINKS IT IS LIKECA WEASEL
    GEN: 052, FITNESS:  93%, MEQHINKS IT IS LIKECA WEASEL
    GEN: 053, FITNESS:  93%, MEQHINKS IT IS LIKEXA WEASEL
    GEN: 054, FITNESS:  93%, MEQHINKS IT IS LIKEXA WEASEL
    GEN: 055, FITNESS:  93%, MEQHINKS IT IS LIKEXA WEASEL
    GEN: 056, FITNESS:  93%, MEQHINKS IT IS LIKEXA WEASEL
    GEN: 057, FITNESS:  93%, MEQHINKS IT IS LIKEXA WEASEL
    GEN: 058, FITNESS:  93%, MEQHINKS IT IS LIKENA WEASEL
    GEN: 059, FITNESS:  93%, MEQHINKS IT IS LIKENA WEASEL
    GEN: 060, FITNESS:  96%, MEQHINKS IT IS LIKE A WEASEL
    GEN: 061, FITNESS:  96%, MEQHINKS IT IS LIKE A WEASEL
    GEN: 062, FITNESS:  96%, MEQHINKS IT IS LIKE A WEASEL
    GEN: 063, FITNESS:  96%, MEQHINKS IT IS LIKE A WEASEL
    GEN: 064, FITNESS:  96%, MEQHINKS IT IS LIKE A WEASEL
    GEN: 065, FITNESS:  96%, MEQHINKS IT IS LIKE A WEASEL
    GEN: 066, FITNESS:  96%, MEQHINKS IT IS LIKE A WEASEL
    GEN: 067, FITNESS:  96%, MEQHINKS IT IS LIKE A WEASEL
    GEN: 068, FITNESS:  96%, MEQHINKS IT IS LIKE A WEASEL
    GEN: 069, FITNESS:  96%, MEQHINKS IT IS LIKE A WEASEL
    GEN: 070, FITNESS:  96%, MEQHINKS IT IS LIKE A WEASEL
    GEN: 071, FITNESS:  96%, MEQHINKS IT IS LIKE A WEASEL
    GEN: 072, FITNESS:  96%, MEQHINKS IT IS LIKE A WEASEL
    GEN: 073, FITNESS:  96%, MEQHINKS IT IS LIKE A WEASEL
    GEN: 074, FITNESS: 100%, METHINKS IT IS LIKE A WEASEL
    Elapsed time: 0.0408 seconds

```bash
$ python -m timeit -c "$(cat weasel.py)" | tail -1
```

    10 loops, best of 5: 31.8 msec per loop

... or 0.0318 seconds per loop

## Profile

```bash
$ python -m cProfile -o weasel.prof weasel.py
$ python -m pstats weasel.prof
```

    Welcome to the profile statistics browser.
    weasel.prof% strip
    weasel.prof% sort cumtime
    weasel.prof% stats 15
    Tue Jun  6 12:12:34 2023    weasel.prof

            465308 function calls (465215 primitive calls) in 0.545 seconds

    Ordered by: cumulative time
    List reduced from 211 to 15 due to restriction <15>

    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     4/1    0.000    0.000    0.545    0.545 {built-in method builtins.exec}
     1      0.000    0.000    0.545    0.545 weasel.py:1(<module>)
     1      0.001    0.001    0.539    0.539 weasel.py:42(main)
     74     0.009    0.000    0.532    0.007 {built-in method builtins.max}
     6464   0.008    0.000    0.287    0.000 weasel.py:52(<genexpr>)
     6400   0.008    0.000    0.279    0.000 weasel.py:33(reproduce)
     6400   0.120    0.000    0.270    0.000 weasel.py:34(<listcomp>)
     6465   0.015    0.000    0.238    0.000 weasel.py:37(fitness)
     6465   0.104    0.000    0.220    0.000 {built-in method builtins.sum}
    187485  0.115    0.000    0.115    0.000 weasel.py:38(<genexpr>)
    179228  0.090    0.000    0.090    0.000 {method 'random' of '_random.Random' objects}
     8823   0.022    0.000    0.060    0.000 random.py:367(choice)
     8823   0.018    0.000    0.029    0.000 random.py:235(_randbelow_with_getrandbits)
     24255  0.013    0.000    0.013    0.000 {built-in method builtins.len}
     10463  0.006    0.000    0.006    0.000 {method 'getrandbits' of '_random.Random' objects}
