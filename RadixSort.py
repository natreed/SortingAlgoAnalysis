#Implementation of radix sort algorithm in python http://en.wikipedia.org/wiki/Radix_sort
import Sort

import math
import Util
import time

class RadixSort():
    def __init__(self, intList):
        self.intList = intList;
    def sort(self, list):
        listLength = len(list)
        modulus = 10
        div = 1
        while True:
        # empty array, [[] for i in range(10)]
            new_list = [[], [], [], [], [], [], [], [], [], []]
            for value in list:
                least_digit = value % modulus
                least_digit /= div
                new_list[math.floor(least_digit)].append(value)
            modulus = modulus * 10
            div = div * 10

            if len(new_list[0]) == listLength:
                self.intlist = new_list
                return new_list[0]

            list = []
            rd_list_append = list.append
            for x in new_list:
                for y in x:
                    rd_list_append(y)


L = Util.generateList()

def forTime(L):
    A = RadixSort(L)
    Start = time.time()
    M = A.sort(L)
    runTime = time.time() - Start
    #print(M)
    return runTime

#print(forTime(L))
