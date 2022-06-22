import math
from sys import stdin

def main():
    output = []
    for line in stdin:
        necklaces = []
        values = []
        count = 0
        vals = line.split()
        for i in vals:
            values += [int(i)]
        if len(values) == 0:
            print(0,0)
        elif len(values) == 1:
            print(values[0], 0)
        elif len(values) == 2:
            d1 = int(max(values))
            d2 = int(sum(values) - d1)
            print(d1, d2)
        else:
            d1 = int(getNecklaces(values))
            d2 = int(sum(values) - d1)
            print(d1, d2)

def getNecklaces(values):
    lList = values[0:-1]
    rList = values[1:]
    lSum = [0] * len(lList)
    lSum[0] = lList[0]
    rSum = [0] * len(rList)
    rSum[0] = rList[0]
    for i in range(1,len(lList)):
        if i < 2:
            if lList[i] > lList[i-1]:
                lSum[i] = lList[i]
            else:
                lSum[i] = lList[i-1]

            if rList[i] > rList[i-1]:
                rSum[i] = rList[i]
            else: 
                rSum[i] = rList[i-1]
        else:
            if (lSum[i-1] >  (lList[i] + lSum[i-2])):
                lSum[i] = lSum[i-1]
            else:
                lSum[i] = lList[i] + lSum[i-2]

            if (rSum[i-1] > (rList[i] + rSum[i-2])):
                rSum[i] = rSum[i-1]
            else:
                rSum[i] = rList[i] + rSum[i-2]

    return(max(lSum[-1], rSum[-1]))

    


main()