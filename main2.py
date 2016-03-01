import Util
import RadixSort
import HeapSort
import InsertionSort
import MergeSort
import QuickSort
import PythonSorted
import SelectionSort

import time
L = []
A = QuickSort.QuickSort(L)
B = HeapSort.HeapSort(L)
C = InsertionSort.InsertionSort(L)
D = MergeSort.MergeSort(L)
E = PythonSorted.PythonSorted(L)
F = RadixSort.RadixSort(L)
#G = SelectionSort.SelectionSort(L)

#sortList = [A, B, C, D, E, F, G]
#sortNames = ['Quick', 'Heap', 'Insertion', 'Merge', 'Python', 'Radix', 'Selection']

sortList = [A, B, C, D, E, F]
sortNames = ['Quick', 'Heap', 'Insertion', 'Merge', 'Python', 'Radix']

def printTimes(timesList):
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
    print("radix sort")
    print(timesList[5])
    #print("selection sort")
    #print(timesList[6])
    print('\n')
#sortList = [C]
#sortNames = ['Insertion']


sizeList = [20, ]
#sizeList = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000, 10000, 20000, 50000]
timesList = [[], [], [], [], [], [], []]

#for i in range(len(sizeList)):


timesList = [[], [], [], [], [], [], []]
for j in range(len(sortList)):
    for i in range(len(sizeList)):
        L = Util.generateReversed(sizeList[i])
        Start = time.time()
        M = sortList[j].sort(L)
        runTime = (time.time() - Start) * 1000000
        runTime = float("{0:.2f}".format(runTime))
        timesList[j].append(runTime)
f = open('ReversedList-Range100XSize.csv', 'w')
f.write('Reversed List. Range 100XSize\n')
for j in range(len(sizeList)):
    f.write(', ' + str(sizeList[j]))
f.write('\n')
for j in range(len(sortNames)):
    f.write(sortNames[j])
    for k in range(len(timesList[j])):
        f.write(", " + str(timesList[j][k]))
    f.write("\n")
printTimes(timesList)