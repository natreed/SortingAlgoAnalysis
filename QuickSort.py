import Util;
import time;
import random;

class QuickSort():
    def __init__(self, intList):
        self.intList = intList;


def sort(L):
    less = [];
    equal = [];
    greater = [];
    if len(L) > 1:
        pivot = random.randrange(0, len(L));
        for x in L:
            print(x, L[pivot])
            if x < L[pivot]:
                less.append(x);
            elif x == L[pivot]:
                equal.append(x);
            else:
                greater.append(x);
        return sort(less) + equal + sort(greater);

    else:
        return L;


for i in range(10):
    L = Util.generateList();
    A = QuickSort(L);
    Start = time.time();
    sort(L);
    runTime = time.time() - Start;
    if i == 0:
        print(A.intList)
    print(runTime);