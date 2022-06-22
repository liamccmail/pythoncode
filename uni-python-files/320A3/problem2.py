import math

def main():
    n = int(input())
    intervalTestCases = []
    for i in range(n):
        intervals = []
        starts = []
        finishes = []
        times = input()
        times = [int(i) for i in times.split(' ') if i.isdigit()]
        count = 0
        while count != len(times):
            starts += [times[count]]
            finishes += [times[count + 1]]
            count += 2
        starts.sort()
        finishes.sort()
        intervals += [starts,finishes]
        intervalTestCases += [intervals]
    getOverlaps(intervalTestCases)

def getOverlaps(intervalTestCases):
    for intervals in intervalTestCases:
        intervalsCurr = 1 # Set current intervals to 1 (Will always have 1 interval)
        maxIntervals = 1 # Max default set to 1
        starts = intervals[0] # Partion first index to arrivals
        finishes = intervals[1]
        start = starts[0]
        a = 1 # Pointer for interval start to check against the start
        e = 0 # Pointer for interval finish to check against current start
        while (a < len(starts) and e < len(finishes)):
            if starts[a] <= finishes[e]:
                intervalsCurr += 1 # if the current start interval is less than the current finish, append 1
                if intervalsCurr > maxIntervals:
                    maxIntervals = intervalsCurr # if the current interval is greater than max, make it equal to it
                    start = starts[a] # start is equal to current interval
                a += 1 # increment to next start
            else:
                intervalsCurr -= 1 # decrement to show that intervals have finished
                e += 1 # increment to next finish
        print(maxIntervals)

main()