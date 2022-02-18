import math
import random
import time
from threading import Thread

def randBool():
    return True if random.choice([True, False, False]) else False
    # weight on False is heavier, because it would generate longer cycles

def generateBooleanList(lowerBound, upperBound):
    generatedList = list()
    lengthOfString = random.randint(lowerBound,upperBound)
    for i in range(lengthOfString):
        if randBool():
            generatedList.append(True)
        else:
            generatedList.append(False)
    return generatedList

def algorithm(lowerBound, upperBound):
    numInCycle = 0
    while(True):
        newInitialGuess = generateBooleanList(lowerBound, upperBound)
        changingGuess = newInitialGuess
        guessSequence = []
        terminateSequence = True
        while(terminateSequence):
            if changingGuess[0]:
                changingGuess = changingGuess[3:]
                changingGuess.append(True)
                changingGuess.append(True)
            elif not changingGuess[0]:
                ch = changingGuess[3:]
                changingGuess.append(False)
                changingGuess.append(False)
                changingGuess.append(True)
                changingGuess.append(False)
            if changingGuess in guessSequence:
                endSequence = False
                seqLength = len(guessSequence)
                for i in range(len(guessSequence)):
                    if changingGuess == guessSequence[i] and numInCycle < (seqLength - i - 1):
                        print(f"{changingGuess}, {guessSequence[i]}, {i}")
                        numInCycle = seqLength - i - 1
                        print(f"Start: {newInitialGuess} cycle= {numInCycle}, sequence = {seqLength}")
                        

            else:
                guessSequence.append(changingGuess)
        
            
if __name__ == "__main__":
    lowerBound = int(input("What would you like the lower random bound to be?: "))
    upperBound = int(input("What would you like the upper random bound to be?: "))
    algorithm(lowerBound, upperBound)
    