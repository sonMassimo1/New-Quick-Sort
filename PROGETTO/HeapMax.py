


class HeapMax:

    def __init__(self, l):
        """It takes a list as the parameter
        """
        self.heap = l
        self.length = len(l)

    def isEmpty(self):
        return self.length == 0

    def maxSon(self, fatherId):
        """Returns -1 if father is a leaf
        """
        if fatherId * 2 + 1 > (self.length - 1):  # fatherId non ha figli
            return -1

        if fatherId * 2 + 2 > (self.length - 1):  # fatherId ha un unico figlio ed e' fatherId * 2 +1
            return fatherId * 2 + 1

        if self.heap[fatherId * 2 + 1] > self.heap[
                            fatherId * 2 + 2]:  # fatherId ha due figli e si calcola il piu' grande
            return fatherId * 2 + 1
        else:
            return fatherId * 2 + 2

    def findMax(self):  # trovare l'elemento massimo in un heap e' uguale a restituire la radice dell'heap
        if self.length == 0:
            return None
        else:
            return self.heap[0]

    def moveDown(self, fatherId):

        son = self.maxSon(fatherId)
        while son != -1 and self.heap[son] > self.heap[fatherId]:
            self.heap[son], self.heap[fatherId] = self.heap[fatherId], self.heap[son]
            fatherId = son
            son = self.maxSon(fatherId)

    def deleteMax(self):

        if self.length == 0:
            return None
        # scambia primo ed ultimo elemento
        maxValue = self.heap[0]
        self.heap[0], self.heap[self.length - 1] = self.heap[self.length - 1], self.heap[0]
        self.length -= 1
        self.moveDown(0)  # ripristina l'ordinamento con muoviBasso() sul primo elelemto
        return maxValue

    def heapify(self):

        self.recursiveHeapify(0, self.length - 1)

    def recursiveHeapify(self, first, last):

        if first > last:
            return
        self.recursiveHeapify(2 * first + 1, last)  # rende un heap il sottoalbero sinistro di first
        self.recursiveHeapify(2 * first + 2, last)  # rende un heap il sottoalbero destro di first


        self.moveDown(first)  # ripristina l'ordinamento spostando first verso il basso

