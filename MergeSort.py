import Util;
import time;
import math;
import Sort

class MergeSort():
    def __init__(self, intList):
        self.intList = intList;
    def sort(self, list):
        #L = self.intList;
        n = len(list)
        if n is 1:
            return list
        mid = math.floor(n/2)
        firstHalf = list[0:mid]
        secondHalf = list[mid:n]
        B = self.sort(firstHalf)
        C = self.sort(secondHalf)
        self.intList = self.merge(B, C)
        return self.intList

    def merge(self, B, C):
        i = j = 0
        A = []
        while i < len(B) and j < len(C):
            if B[i] <= C[j]:
                A.append(B[i])
                i += 1
            else:
                A.append(C[j])
                j += 1
        if i == (len(B)):
            for k in range(j, len(C)):
                A.append(C[k])
        else:
            for k in range(i, len(B)):
                A.append(B[k])
        return A


L = Util.generateList(10)


def forTime(L):
    A = MergeSort(L)
    Start = time.time()
    M = A.sort(L)
    runTime = time.time() - Start
    #print(M)
    return runTime

