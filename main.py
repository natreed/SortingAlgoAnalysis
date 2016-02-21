import Util
import RadixSort
import HeapSort
import InsertionSort
import MergeSort
import QuickSort
import PythonSorted
import SelectionSort
import Sort

import time

"""
for i in range(5):
    L = Util.generateList()
    A = QuickSort.QuickSort(L)

"""
timesList = [[], [], [], [], [], [], []]

for i in range(5):
    L = Util.generateList()
    A = QuickSort.QuickSort(L)
    B = HeapSort.HeapSort(L)
    C = InsertionSort.InsertionSort(L)
    D = MergeSort.MergeSort(L)
    E = PythonSorted.PythonSorted(L)
    F = SelectionSort.SelectionSort(L)
    G = RadixSort.RadixSort(L)

    sortList = [A, B, C, D, E, F, G]
    #M = sortList[2].sort(L)
    #print(M)

    for j in range(len(sortList)):
        Start = time.time()
        M = sortList[j].sort(L)
        runTime = (time.time() - Start) * 1000000
        #print(M)
        runTime = float("{0:.2f}".format(runTime))
        timesList[j].append(runTime)

    #print(sortList[2])

print("quicksort")
print(timesList[0])
print("Heap Sort")
print(timesList[1])
print("Insertion sort")
print(timesList[2])
print("Mergesort")
print(timesList[3])
print("PythonSorted")
print(timesList[4])
print("selection sort")
print(timesList[5])
print("radix sort")
print(timesList[6])



