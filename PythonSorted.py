import time
import Util
import Sort

class PythonSorted():
    def __init__(self, intList):
        self.intList = intList

    def sort(self, intList):
        self.intList = sorted(intList)
        return self.intList




L = Util.generateList(10)

def forTime(L):
    A = PythonSorted(L)
    Start = time.time()
    M = A.sort(L)
    runTime = time.time() - Start
    return runTime

#print(forTime(L))

