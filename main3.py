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
#C = InsertionSort.InsertionSort(L)
D = MergeSort.MergeSort(L)
E = PythonSorted.PythonSorted(L)
F = RadixSort.RadixSort(L)
#G = SelectionSort.SelectionSort(L)

sortList = [A, B, D, E, F]
sortNames = ['Quick', 'Heap', 'Merge', 'Python', 'Radix']



#sortList = [A, B, C, D, E, F]
#sortNames = ['Quick', 'Heap', 'Insertion', 'Merge', 'Python', 'Radix']

def printTimes(timesList):
    print("quicksort")
    print(timesList[0])
    print("Heap Sort")
    print(timesList[1])
    #print("Insertion sort")
    #print(timesList[2])
    print("Mergesort")
    print(timesList[2])
    print("PythonSorted")
    print(timesList[3])
    print("radix sort")
    print(timesList[4])
    #print("selection sort")
    #print(timesList[6])
    print('\n')
#sortList = [C]
#sortNames = ['Insertion']

#sizeList = [8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
#sizeList = [500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]
sizeList = [16384, 32768, 65536, 131072, 262144, 524288, 1048576]
timesList = [[], [], [], [], []]

#for i in range(len(sizeList)):



for i in range(len(sizeList)):
    L = Util.generateList(sizeList[i])
    for j in range(len(sortList)):
        N = list(L)
        Start = time.time()
        M = sortList[j].sort(N)
        runTime = (time.time() - Start) * 1000000
        runTime = float("{0:.2f}".format(runTime))
        timesList[j].append(runTime)
        #print(M)
f = open('RandomSizeList-LargeValues.csv', 'w')
f.write('Random Size List. Range 100XSize \n')
for j in range(len(sizeList)):
    f.write(', ' + str(sizeList[j]))
f.write('\n')
for j in range(len(sortNames)):
    f.write(sortNames[j])
    for k in range(len(timesList[j])):
        f.write(", " + str(timesList[j][k]))
    f.write("\n")
printTimes(timesList)

timesList = [[], [], [], [], [], [], []]
for i in range(len(sizeList)):
    L = Util.generateSorted(sizeList[i])
    for j in range(len(sortList)):
        N = list(L)
        Start = time.time()
        M = sortList[j].sort(N)
        runTime = (time.time() - Start) * 1000000
        runTime = float("{0:.2f}".format(runTime))
        timesList[j].append(runTime)
        #print(M)
f = open('SortedList-LargeValues.csv', 'w')
f.write('Sorted List. Range 100XSize\n')
for j in range(len(sizeList)):
    f.write(', ' + str(sizeList[j]))
f.write('\n')
for j in range(len(sortNames)):
    f.write(sortNames[j])
    for k in range(len(timesList[j])):
        f.write(", " + str(timesList[j][k]))
    f.write("\n")
printTimes(timesList)

timesList = [[], [], [], [], [], [], []]
for i in range(len(sizeList)):
    L = Util.generateReversed(sizeList[i])
    for j in range(len(sortList)):
        N = list(L)
        Start = time.time()
        M = sortList[j].sort(N)
        runTime = (time.time() - Start) * 1000000
        runTime = float("{0:.2f}".format(runTime))
        timesList[j].append(runTime)
        #print(M)
f = open('ReversedList-LargeValues.csv', 'w')
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


timesList = [[], [], [], [], [], [], []]
for i in range(len(sizeList)):
    L = Util.generateSmallRange(sizeList[i])
    for j in range(len(sortList)):
        N = list(L)
        Start = time.time()
        M = sortList[j].sort(N)
        runTime = (time.time() - Start) * 1000000
        runTime = float("{0:.2f}".format(runTime))
        timesList[j].append(runTime)
        #print(M)
f = open('LittleRange-one-thru-twenty_Large.csv', 'w')
f.write('Small Range (20)\n')
for j in range(len(sizeList)):
    f.write(', ' + str(sizeList[j]))
f.write('\n')
for j in range(len(sortNames)):
    f.write(sortNames[j])
    for k in range(len(timesList[j])):
        f.write(", " + str(timesList[j][k]))
    f.write("\n")
printTimes(timesList)
