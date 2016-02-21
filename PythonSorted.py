import time
import Util
import Sort

class PythonSorted():
    def __init__(self, intList):
        self.intList = intList

    def sort(self, intList):
        self.intList = sorted(intList)
        return self.intList

L = Util.generateList()

def forTime(L):
    A = PythonSorted(L)
    Start = time.time()
    M = A.sort(L)
    runTime = time.time() - Start
    #print(M)
    return runTime

#print(forTime(L))