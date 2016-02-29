import Util;
import time;
import random;
import Sort

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
        return self.intList

L = Util.generateList(10)


def forTime(L):
    A = QuickSort(L)
    Start = time.time()
    M = A.sort(L)
    runTime = time.time() - Start
    #print(M)
    return runTime

#print(forTime(L))



"""
for i in range(10):
    L = Util.generateList()
    A = QuickSort(L)
    Start = time.time()
    A.sort(L)
    runTime = time.time() - Start

    print(runTime)



Quicksort is a divide and conquer algorithm. Quicksort first divides a large array into two smaller sub-arrays: the low elements and the high elements. Quicksort can then recursively sort the sub-arrays.

The steps are:

Pick an element, called a pivot, from the array.
Partitioning: reorder the array so that all elements with values less than the pivot come before the pivot, while all elements with values greater than the pivot come after it (equal values can go either way). After this partitioning, the pivot is in its final position. This is called the partition operation.
Recursively apply the above steps to the sub-array of elements with smaller values and separately to the sub-array of elements with greater values.
The base case of the recursion is arrays of size zero or one, which never need to be sorted.

The pivot selection and partitioning steps can be done in several different ways; the choice of specific implementation schemes greatly affects the algorithm's performance.

"""
