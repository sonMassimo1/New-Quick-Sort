from collections import deque
import sys
import os

sys.path.append(str(os.environ.get("PYTHONPATH")) + "/Lez2/")
# to import a library from a directory that isn't the current one
# it needs to specify the path
# $PYTHONPATH is the environment variable containing the project home

from LinkedList import ListaCollegata


class CodaListaCollegata(ListaCollegata):
    def enqueue(self, elem):
        self.addAsLast(elem)

    def dequeue(self):
        return self.popFirst()


class CodaArrayList():
    def __init__(self):
        self.q = []

    def enqueue(self, elem):
        self.q.append(elem)

    def dequeue(self):
        if len(self.q) == 0:
            return None
        return self.q.pop(0)

    def getFirst(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[0]

    def isEmpty(self):
        return len(self.q) == 0

    def printOrdered(self):
        print("Elements in the collection (ordered):")
        print(self.q)


class CodaArrayList_deque(CodaArrayList):
    def __init__(self):
        super().__init__()
        self.q = deque()

    # Override
    def dequeue(self):
        if len(self.q) == 0:
            return None
        return self.q.popleft()


# global functions
def testQueue(q):
    for i in range(10):
        q.enqueue(i)
    q.printOrdered()

    print("First:", q.getFirst())
    print("Dequeue:", q.dequeue())
    print("First:", q.getFirst())
    print("Dequeue:", q.dequeue())
    print("First:", q.getFirst())

    q.printOrdered()


# to run this module directly (NOT imported in another one)
if __name__ == "__main__":
    print("Coda - ListaCollegata")
    q = CodaListaCollegata()
    testQueue(q)

    print("Coda - ArrayList")
    q = CodaArrayList()
    testQueue(q)

    print("Coda - ArrayList_deque")
    q = CodaArrayList_deque()
    testQueue(q)
