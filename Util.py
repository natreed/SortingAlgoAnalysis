#Generate arrays
import random;
import sys;
import math


def generateList(listSize):
    randList = list(range(0, listSize));
    for i in randList:
        randList[i] = random.randrange(0, listSize*100);
    return randList

def generateSorted(listSize):
    L = generateList(listSize)
    M = sorted(L)
    return M

def generateReversed(listSize):
    L = generateList(listSize)
    M = sorted(L)
    M.reverse()
    return M

def generateSmallRange(listSize):
    randList = list(range(0, listSize));
    for i in randList:
        randList[i] = random.randrange(0, 20);
    return randList


#M = generateSmallRange(100)
#print(M)
