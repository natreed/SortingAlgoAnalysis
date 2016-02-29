import Util;
import time;

class SelectionSort():
    def __init__(self, intList):
        self.intList = intList;
    def sort(self, intList):
        L = intList
        for i in range(len(L)):
            least = i;
            for j in range(i+1, len(L)):
                if L[j] < L[least]:
                    least = j
            self.swap(L, i, least)
            self.intList = L
        return self.intList

    def swap(self, A, x, y):
        temp = A[x]
        A[x] = A[y]
        A[y] = temp


"""
for i in range(10):
    L = Util.generateList(10);
    A = SelectionSort(L);
    Start = time.time();
    A.sort(L);
    runTime = time.time() - Start;
    if i == 0:
        print(A.intList)
    print(runTime);
    """


