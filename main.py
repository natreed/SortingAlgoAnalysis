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
sizeList = [10, 50]

for i in range(len(sizeList)):
    L = Util.generateList(sizeList[i])
    M = Util.generateSorted(sizeList[i])
    N = Util.generateReversed(sizeList[i])
    O = Util.generateSmallRange(sizeList[i])

    #listList = [L, M, N, O]
    #listNames = ['Random', 'Sorted', 'Reversed', 'SmallRange']
    listList = [L, M, O]
    listNames = ['Random', 'Sorted',  'SmallRange']
    timesList = [[], [], [], [], [], [], []]
    for x in range(len(listList)):
        #L = listList[x]
        L = Util.generateList(sizeList[i])
        A = QuickSort.QuickSort(L)
        B = HeapSort.HeapSort(L)
        C = InsertionSort.InsertionSort(L)
        D = MergeSort.MergeSort(L)
        E = PythonSorted.PythonSorted(L)
        F = SelectionSort.SelectionSort(L)
        G = RadixSort.RadixSort(L)

        sortList = [A, B, C, D, E, F, G]
        sortNames = ['Quick', 'Heap', 'Insertion', 'Merge', 'Python', 'Selection', 'Radix']

        #sortList = [C]
        #sortNames = ['Insertion']

        for j in range(len(sortList)):
            Start = time.time()
            M = sortList[j].sort(L)
            runTime = (time.time() - Start) * 1000000
            runTime = float("{0:.2f}".format(runTime))
            timesList[j].append(runTime)

            #print(sortList[2])
        if listNames[x] is 'Random':
            f = open('RandomSizeList-Range100XSize.csv', 'w')
            f.write('Random Size List. Range 100XSize \n')
        elif listNames[x] is 'Sorted':
            f = open('SortedList-Range100XSize.csv', 'w')
            f.write('Sorted List. Range 100XSize\n')
        elif listNames[x] is 'Reversed':
            f = open('ReversedList-Range100XSize.csv', 'w')
            f.write('Reversed List. Range 100XSize\n')
        else:
            assert listNames[x] is 'SmallRange'
            f = open('LittleRange-Range_one_fifth_XSize.csv', 'w')
            f.write('Small Range. 1/5 List Size\n')

        for j in range(len(sizeList)):
            f.write(', ' + str(sizeList[j]))
        f.write('\n')
        for j in range(len(sortNames)):
            f.write(sortNames[j])
            for k in range(len(timesList[j])):
                f.write(", " + str(timesList[j][k]))
            f.write("\n")


        print('\n\n' + listNames[x])
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


