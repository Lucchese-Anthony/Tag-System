# Tag-System

These programs were made in tandem with my Chaos and Fractals course, MATH320, where we were to solve [Post Tag's system]{https://en.wikipedia.org/wiki/Tag_system}

This system has 3 states:

            |   n                   if len(n) < 3
    T(n) if |   n[3...n] + aa       if n[0] = 'a'
            |   n[3...n] + bbab     if n[0] = 'b'


so as an example we will assume the string "aabba"

    aabba => baaa => abbab (cycle found abbab)

or "bbb"
    
    bbb => bbab => bbbab => abbbab => babaa => aabbab => babaa => aabbab (cycle found aabbab)

solveSingleTagSystem.py solves a single Tag System provided by the user

generateRandomTagSystem.py generates random Systems to find the longest cycle possible (not properly optimized, O(n^2) i believe)
