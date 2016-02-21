import Util;
import time;

class SelectionSort():
    def __init__(self, intList):
        self.intList = intList;
    def sort(self, intList):
        L = self.intList;
        for i in range(len(L)):
            least = i;
            for j in range(i+1, len(L)):
                if L[j] < L[least]:
                    least = j;
            self.swap(L, i, least);
        return self.intList

    def swap(self, A, x, y):
        temp = A[x];
        A[x] = A[y];
        A[y] = temp;

L = Util.generateList()


def forTime(L):
    A = SelectionSort(L)
    Start = time.time()
    M = A.sort(L)
    runTime = time.time() - Start
    #print(M)
    return runTime

#print(forTime(L))


