#Generate arrays
import random;
import sys;



def generateList():
    randList = list(range(0, 10));
    for i in randList:
        randList[i] = random.randrange(0, 1000);
    return randList