import random
import time
from PROGETTO.Sorting import mergeSort
from math import ceil

def NewQuickSort(l, quick):#parametro quick per scegliere tipologia di quick
    recursiveNewQuickSort(l, 0, len(l) - 1, quick)


def recursiveNewQuickSort(l, left, right, quick):


    if left >= right:
        return

    mid = partition(l, left, right, quick)
    recursiveNewQuickSort(l, left, mid - 1, quick)
    recursiveNewQuickSort(l, mid + 1, right, quick)




def partition(l, left, right, quick):
    inf = left
    sup = right + 1

    if quick==0:
        random.seed(1)
        mid = random.randint(left, right)
        l[left], l[mid] = l[mid], l[left]
    elif quick==2:

        numElem = right - left +1
        if len(l)>=500:
            m = int(ceil(numElem * 0.01)) # valore di m pari al 1% di l se l supera i 500 elementi
        else:
            m = int(ceil(numElem * 0.10)) #valore di m pari al 10% di l se l è sotto i 500 elementi
        sampleMedianSelect(l, left, right, m)
    mid = left



    while True:
        inf += 1
        while inf <= right and l[inf] <= l[mid]:
            inf += 1

        sup -= 1
        while l[sup] > l[mid]:
            sup -= 1

        if inf < sup:
            l[inf], l[sup] = l[sup], l[inf]
        else:
            break

    l[mid], l[sup] = l[sup], l[mid]



    return sup

def sampleMedianSelect(l, left, right, m):
    V=[]
    for x in range(0,m):
        rand=random.randint(left, right)
        Velem=(l[rand], rand)  # creo un tupla contenente valore e indice
        V.append(Velem)
    mergeSort(V)  #ordino tramite mergesort
    pivot=V[int(m/2)][1]
    l[left], l[pivot] = l[pivot], l[left]
    return


def Array():  #funzione per test, genera array di diverse misure in modo randomico
    A=[]
    for i in range(0,10):
        A.append(random.randint(0,10000))
    return A

if __name__ == '__main__':
     l=Array()
     #l=[] array vuoto
     #l=[1,2,3,4,5,6,7,8,9] array ordinato
     #l=[9,8,7,6,5,4,3,2,1]  prove effettuate array ordinato crescente
     print(l)
     start=time.time()
     NewQuickSort(l,2)   #quick=0 quick rand, se quick!=0e2 quick det, se quick=2 samplemedianselect
     print(time.time()-start)
     print(l)



##tempo peggiore n quadro tempo migliore nlogn tempo medio nlogn
