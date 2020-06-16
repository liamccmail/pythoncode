import math

def main():
    n = int(input())
    intervalTestCases = []
    for i in range(n):
        intervals = []
        times = input()
        times = [int(i) for i in times.split(' ') if i.isdigit()]
        count = 0 
        while count != len(times):
            intervals += [[times[count], times[count + 1]]]
            count += 2
        intervals.sort(key = lambda x: x[0])
        intervalTestCases += [intervals]
    for i in intervalTestCases:
        maxContiguous = getLargestContiguousV1(i)
        print(maxContiguous)

def getLargestContiguousV1(interval):
    contiguousIntervals = []
    nextCheck = interval[0]
    contiguousIntervals += [interval[0]]
    for i in range(1, len(interval)):
        if contiguousIntervals[-1][1] < interval[i][0] :
            contiguousIntervals += [interval[i]]
        elif contiguousIntervals[-1][1] < interval[i][1]:
            contiguousIntervals[-1] = [contiguousIntervals[-1][0], interval[i][1]]
    setOfIntervals = []
    for i in contiguousIntervals:
        setOfIntervals += [i[1] - i[0]]
    maxContiguous = max(setOfIntervals)
    return maxContiguous

main()