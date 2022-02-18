import math
import random
import time
from threading import Thread

def main():
    numInCycle = 0
    inputGuess = str(input(":> "))
    sequence = [inputGuess]
    endSequence = True
    with open("TagProblem-Output.txt", "a") as o:
        o.write("[ ")
        while(endSequence):
            if inputGuess[0] == "a":
                inputGuess = inputGuess[3:] + "aa"
            elif inputGuess[0] == 'b':
                inputGuess = inputGuess[3:] + "bbab"
            if len(inputGuess) < 3:
                break
            elif inputGuess in sequence:
                o.write("")
            else:
                sequence.append(inputGuess)
                o.write(inputGuess + ",\n")
        o.write("]")


if __name__ == "__main__":
    main()
    print("\nDone!")