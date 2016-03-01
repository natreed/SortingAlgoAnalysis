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
    randList = list(range(0, 20));
    for i in randList:
        randList[i] = random.randrange(0, listSize);
    return randList


"""
def invertedList(listSize):
    L = generateList(listSize)
    firstHalf = len(L)//2
    lower = L[:(firstHalf)]
    print(lower)
    upper = L[(firstHalf + 1):]
    print(upper)
    lr = generateReversed(lower)
    rs = sorted(upper)
    return (lr + rs)

print(invertedList(20))

"""
