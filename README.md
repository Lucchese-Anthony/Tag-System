# Tag-System

These programs were made in tandem with my Chaos and Fractals course, MATH320, where we were to solve Post Tag's system

This system has 3 states:

            |   n                   if len(n) < 3
    T(n) if |   n[3...n] + aa       if n[0] = 'a'
            |   n[3...n] + bbab     if n[0] = 'b'


so as an example we will assume the string "aabba"

    aabba => baaa => abbab (cycle found abbab)

or "bbb"
    
    bbb => bbab => bbbab => abbbab => babaa => aabbab => babaa => aabbab (cycle found aabbab)