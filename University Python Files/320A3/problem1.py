import math

def main():
    n = int(input())
    intervalTestCases = []
    maxNumNonOverlapIntervals = []
    for i in range(n):
        intervals = []
        times = input()
        times = [int(i) for i in times.split(' ') if i.isdigit()]
        count = 0
        while count != len(times):
            intervals += [[times[count], times[count+1]]]
            count += 2
        intervals.sort(key=lambda x: x[1])
        intervalTestCases += [intervals]
    for i in intervalTestCases:
        j = maxOverlaps(i)
        print(j)

def maxOverlaps(intervals):
    nonOverlappedIntervals = []
    pointer = intervals[0][1]
    count = 0
    for interval in intervals:
        if count == 0:
            nonOverlappedIntervals += [interval[1]]
            count += 1
        else:
            pointer = max(nonOverlappedIntervals)
            if interval[0] > pointer and interval[1] > pointer:
                nonOverlappedIntervals += [interval[1]]
    return len(nonOverlappedIntervals)

main()