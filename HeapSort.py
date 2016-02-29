#http://stackoverflow.com/questions/13979714/heap-sort-how-to-sort
import Util
import time
import Sort


class HeapSort():
    def __init__(self, intList):
        self.intList = intList

    def swap(self, i, j):
        sqc = self.intList
        sqc[i], sqc[j] = sqc[j], sqc[i]

    def heapify(self, end,i):
        sqc = self.intList
        l = 2 * i + 1
        r = 2 * (i + 1)
        max = i
        if l < end and sqc[i] < sqc[l]:
            max = l
        if r < end and sqc[max] < sqc[r]:
            max = r
        if max != i:
            self.swap(i, max)
            self.heapify(end, max)

    def sort(self, intList):
        self.intList = intList
        end = len(self.intList)
        start = end // 2 - 1 # use // instead of /
        for i in range(start, -1, -1):
            self.heapify(end, i)
        for i in range(end-1, 0, -1):
            self.swap(i, 0)
            self.heapify(i, 0)
        return self.intList

L = Util.generateList(10)


def forTime(L):
    A = HeapSort(L)
    Start = time.time()
    M = A.sort(L)
    runTime = time.time() - Start
    print(M)
    return runTime

#print(forTime(L))

"""


for i in range(10):
    L = Util.generateList();
    A = HeapSort(L);
    Start = time.time();
    M = A.sort(L)
    runTime = time.time() - Start;
    print(M)
    print(runTime);


The heapsort algorithm involves preparing the list by first turning it into a max heap. The algorithm then repeatedly swaps the first value of the list with the last value, decreasing the range of values considered in the heap operation by one, and sifting the new first value into its position in the heap. This repeats until the range of considered values is one value in length.

The steps are:

Call the buildMaxHeap() function on the list. Also referred to as heapify(), this builds a heap from a list in O(n) operations.
Swap the first element of the list with the final element. Decrease the considered range of the list by one.
Call the siftDown() function on the list to sift the new first element to its appropriate index in the heap.
Go to step (2) unless the considered range of the list is one element.
The buildMaxHeap() operation is run once, and is O(n) in performance. The siftDown() function is O(log(n)), and is called n times.
Therefore, the performance of this algorithm is O(n + n * log(n)) which evaluates to O(n log n).
"""

