# We need the time module to create some time difference between each comparison
import time

# Importing colors from colors.py
from colors import *

def quickSort(data,drawData, timeTick):
    quickSortHelper(data, 0, len(data)-1, drawData, timeTick)
    drawData(data, [BLUE for x in range(len(data))])

def quickSortHelper(data, startIdx, endIdx, drawData, timeTick):
	if startIdx > endIdx:
		return
	pivotIdx = startIdx
	leftIdx = startIdx + 1
	rightIdx = endIdx
	while rightIdx >= leftIdx:
		if data[leftIdx] > data[pivotIdx] and data[rightIdx] < data[pivotIdx]:
			swap(leftIdx, rightIdx, data, drawData, timeTick)
		if data[leftIdx] <= data[pivotIdx]:
			leftIdx += 1
		if data[rightIdx] >= data[pivotIdx]:
			rightIdx -= 1
	swap(pivotIdx, rightIdx, data, drawData, timeTick)
	leftSubdataIsSmaller = rightIdx - 1 - startIdx < endIdx - (rightIdx+1)
	if leftSubdataIsSmaller:
		quickSortHelper(data, startIdx, rightIdx-1, drawData, timeTick)
		quickSortHelper(data, rightIdx+1, endIdx, drawData, timeTick)
	else:
		quickSortHelper(data, rightIdx+1, endIdx, drawData, timeTick)
		quickSortHelper(data, startIdx, rightIdx - 1, drawData, timeTick)

def swap(i,j,data,drawData,timeTick):
    data[i], data[j] = data[j], data[i]
    drawData(data, [YELLOW if x == i or x == j else BLUE for x in range(len(data))] )
    time.sleep(timeTick)
	

