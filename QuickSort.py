import Util;
import time;
import random;

class QuickSort():
    def __init__(self, intList):
        self.intList = intList;


    def quickSort(self, L):
        less = [];
        equal = [];
        greater = [];
        if len(L) > 1:
            pivot = random.randrange(0, len(L))
            for x in L:
                if x < L[pivot]:
                    less.append(x)
                elif x == L[pivot]:
                    equal.append(x)
                else:
                    greater.append(x)
            return self.quickSort(less) + equal + self.quickSort(greater)

        else:
            return L;

    def sort(self, L):
        self.intList = self.quickSort(L)


for i in range(10):
    L = Util.generateList()
    A = QuickSort(L)
    Start = time.time()
    A.sort(L)
    runTime = time.time() - Start
    if i == 0:
        print(L)
        print(A.intList)
    print(runTime)