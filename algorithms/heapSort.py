# We need the time module to create some time difference between each comparison
import time

# Importing colors from colors.py
from colors import *

def heapSort(data, drawData, timeTick):
    buildMaxHeap(data, drawData, timeTick)
    for endIdx in reversed(range(1, len(data))):
        swap(0, endIdx, data, drawData, timeTick)
        siftDown(0, endIdx - 1, data, drawData, timeTick)
    drawData(data, [BLUE for x in range(len(data))])

def buildMaxHeap(data, drawData, timeTick):
    firstParentIdx = (len(data)-2) // 2
    for currentIdx in reversed(range(firstParentIdx + 1)):
        siftDown(currentIdx, len(data)-1, data, drawData, timeTick)
		
def siftDown(currentIdx, endIdx, heap, drawData, timeTick):
    childOneIdx = currentIdx * 2 + 1
    while childOneIdx <= endIdx:
        childTwoIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
        if childTwoIdx > -1 and heap[childTwoIdx] > heap[childOneIdx]:
            idxToSwap = childTwoIdx
        else:
            idxToSwap = childOneIdx
        if heap[idxToSwap] > heap[currentIdx]:
            swap(currentIdx, idxToSwap, heap, drawData, timeTick)
            currentIdx = idxToSwap
            childOneIdx = currentIdx * 2 + 1
        else:
            return
	
def swap(i,j,data,drawData,timeTick):
    data[i], data[j] = data[j], data[i]
    drawData(data, [YELLOW if x == i or x == j else BLUE for x in range(len(data))] )
    time.sleep(timeTick)
