import time
from colors import *

def insertion_sort(data, drawData, timeTick):
    for i in range(1,len(data)):
        j = i
        while j > 0 and data[j] < data[j-1]:
            swap(j,j-1,data,drawData,timeTick)
            j -= 1
    drawData(data, [BLUE for x in range(len(data))])
def swap(i, j, data, drawData, timeTick):
    data[i],data[j] = data[j],data[i]
    drawData(data, [YELLOW if x == i or x == j else BLUE for x in range(len(data))] )
    time.sleep(timeTick)




