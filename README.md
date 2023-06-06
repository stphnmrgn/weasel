# Weasel Program, aka Dawkin's Weasel

https://en.wikipedia.org/wiki/Weasel_program

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

## Profile

```bash
$ python -m cProfile -o weasel.prof weasel.py
```

    GEN: 000, FITNESS:   4%, UCFATOVBUOQEHJZWLCVOJEGBFLNL
    GEN: 001, FITNESS:   7%, UCFATOVBUOQEIJZWLCVOJEGBFLNL
    GEN: 002, FITNESS:  11%, UCFATOVBUIQEIJZWLCVOJEGBFLNL
    GEN: 003, FITNESS:  14%, UCFATOVB IQEIJZELCVOJEGBWLNL
    GEN: 004, FITNESS:  18%, UCFATOVB IQEIJZEMCVOJEWBWLNL
    GEN: 005, FITNESS:  21%, MCFATOVB IQEIJZEMCVOJEWBWLNL
    GEN: 006, FITNESS:  25%, MCFATOVB ITEIJZEMCVOJEWBWLNL
    GEN: 007, FITNESS:  29%, MCFATOVB ITEIJZEMCEOJEWBWLNL
    GEN: 008, FITNESS:  32%, MCTATMVB ITEIJZEMCEOJEWBWLNL
    GEN: 009, FITNESS:  32%, MCTATMVB ITEIJZEMCEQJEWBWLNL
    GEN: 010, FITNESS:  36%, MCTATMVB ITEIJZEMCEQJEWBWLEL
    GEN: 011, FITNESS:  39%, METATMVB ITEIJZEMCEQJEWBWLEL
    GEN: 012, FITNESS:  43%, METATMVB IT IJZEMCEQJEWBWLEL
    GEN: 013, FITNESS:  46%, METATMVB IT IJZEICEQJEWBWLEL
    GEN: 014, FITNESS:  50%, METATMVB IT IJZEICEQAEWSWLEL
    GEN: 015, FITNESS:  50%, METATMVB IT IJZEXCEQA WSWLEL
    GEN: 016, FITNESS:  54%, METATNVB IT IJZEPCEQA WSWLEL
    GEN: 017, FITNESS:  57%, METATNVB IT IJ EPCEQA WSWLEL
    GEN: 018, FITNESS:  57%, METATNVB IT IJ EPCEQA WSWLEL
    GEN: 019, FITNESS:  61%, METATNTB IT IS EPCEQA WSWLEL
    GEN: 020, FITNESS:  61%, METATNTB IT IS EPCEQA WSALCL
    GEN: 021, FITNESS:  64%, METATNTB IT IS EPCEQA WSASCL
    GEN: 022, FITNESS:  68%, METATNTS IT IS EPCEQA WSASCL
    GEN: 023, FITNESS:  68%, METATNTS IT IS EPCEQA WSASCL
    GEN: 024, FITNESS:  71%, METATNTS IT IS EPKEQA WSASCL
    GEN: 025, FITNESS:  71%, METAPNNS IT IS YPKEQA WSASTL
    GEN: 026, FITNESS:  71%, METUPNNS IT IS YPKEQA WSASTL
    GEN: 027, FITNESS:  75%, METUPNKS IT IS GPKEWA WSASTL
    GEN: 028, FITNESS:  75%, METUPNKS IT IS GSKEWA WSASTL
    GEN: 029, FITNESS:  79%, METHPNKS IT IS GSKEWA WSASTL
    GEN: 030, FITNESS:  79%, METHPNKS IT IS GSKEWA WSASTL
    GEN: 031, FITNESS:  79%, METHPNKS IT IS GSKEWA WSASTL
    GEN: 032, FITNESS:  82%, METHPNKS IT IS GSKE A WSASDL
    GEN: 033, FITNESS:  82%, MECHPNKS IT IS LSKE A WSASDL
    GEN: 034, FITNESS:  82%, MECHPNKS IT IS LHKE A WSASDL
    GEN: 035, FITNESS:  82%, MECHPNKS IT IS LHKE A WSASDL
    GEN: 036, FITNESS:  82%, MECHPNKS IT IS LHKE A WSASDL
    GEN: 037, FITNESS:  86%, METHPNKS IT IS LHKE A WSASDL
    GEN: 038, FITNESS:  86%, METHPNKS IT IS LHKE A WSASDL
    GEN: 039, FITNESS:  86%, METHPNKS IT IS LHKE A WSASDL
    GEN: 040, FITNESS:  89%, METHPNKS IT IS LIKE A WSASDL
    GEN: 041, FITNESS:  89%, METHPNKS IT IS LIKE A WSASDL
    GEN: 042, FITNESS:  89%, METHPNKS IT IS LIKE A WSASDL
    GEN: 043, FITNESS:  93%, METHINKS IT IS LIKE A WSASDL
    GEN: 044, FITNESS:  93%, METHINKS IT IS LIKE A WSASDL
    GEN: 045, FITNESS:  93%, METHINKS IT IS LIKE A WSASDL
    GEN: 046, FITNESS:  93%, METHINKS IT IS LIKE A WSASDL
    GEN: 047, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 048, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 049, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 050, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 051, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 052, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 053, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 054, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 055, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 056, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 057, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 058, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 059, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 060, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 061, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 062, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 063, FITNESS:  96%, METHINKS IT IS LIKE A WSASEL
    GEN: 064, FITNESS: 100%, METHINKS IT IS LIKE A WEASEL

```bash
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
