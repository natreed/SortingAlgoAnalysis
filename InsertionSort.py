import Util;
import time;
import Sort

class InsertionSort():
    def __init__(self, intList):
        self.intList = intList;
    def sort(self, intList):
        L = self.intList;
        for i in range(1, len(L)):
            j = i;
            while j > 0 and L[j] < L[j-1]:
                self.swap(L, j, (j-1));
                j -= 1;
        return self.intList

    def swap(self, A, x, y):
        temp = A[x];
        A[x] = A[y];
        A[y] = temp;

L = Util.generateList();

def forTime(L):
    A = InsertionSort(L);
    Start = time.time();
    M = A.sort(L);
    runTime = time.time() - Start
    #print(M)
    return runTime

#print(forTime(L))
