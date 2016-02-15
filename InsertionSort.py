import Util;
import time;

class InsertionSort():
    def __init__(self, intList):
        self.intList = intList;
    def sort(self):
        L = self.intList;
        for i in range(1, len(L)):
            j = i;
            while j > 0 and L[j] < L[j-1]:
                self.swap(L, j, (j-1));
                j -= 1;
    def swap(self, A, x, y):
        temp = A[x];
        A[x] = A[y];
        A[y] = temp;

for i in range(10):
    L = Util.generateList();
    A = InsertionSort(L);
    Start = time.time();
    A.sort();
    runTime = time.time() - Start;
    if i == 0:
        print(A.intList)
    print(runTime);