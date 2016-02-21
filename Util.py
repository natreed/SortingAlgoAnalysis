#Generate arrays
import random;
import sys;



def generateList():
    randList = list(range(0, 10000));
    for i in randList:
        randList[i] = random.randrange(0, 10000000000);
    return randList