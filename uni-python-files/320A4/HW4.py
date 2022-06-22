import math
import random
import sys

def main():
    probabilityOfSpamEntry = 1 - math.exp(-1/8)
    A = list() # {1, 2, ... 1000000}
    for i in range(1000000):
        A += [i]
    B = list() # List of 0s
    for i in range(8000000):
        B += [0]
    spamList = list()
    for i in range(1000):
        spam = random.randint(1000001,sys.maxsize)
        spamList += [spam]
    p = 9000059
    n = len(B)
    a = random.randint(0,p)
    b = random.randint(0,p)
    tAddrIn = hash(A,B, p, n, a, b)
    indexesOf1s = 0
    for i in B:
        if i == 1:
            indexesOf1s += 1
    tAddr = (tAddrIn // len(A)) * 100

    actualProbabilityOfSpam = indexesOf1s / len(B)
    print('\nQ1.\nNumber of Trusted Addresses:', 
    str(tAddr) + '%')
    print("Number of collisions:" ,str(len(A) - indexesOf1s),"\n")

    print("Q2.\nPr that a spam address goes through:", 
    probabilityOfSpamEntry * 100)
    print("Theorectical Pr that a spam address goes through:", 
    actualProbabilityOfSpam * 100, "\n")

    spamLetIn = checkForSpam(spamList, B, p, n, a, b)
    percentageOfSpam = ((spamLetIn / len(spamList)) * 100)
    print("Q3.\nSpam addresses that go through:", 
    str(percentageOfSpam) + "%", "of 1000 Addresses\n")
    

def hash(A, B, p, n, a, b):
    count = 0
    for i in A:
        hashFunc = (((a * i)+ b) % p) % n
        count += 1
        B[hashFunc] = 1
    return count

def checkForSpam(spamList, B, p, n, a, b):
    count = 0
    for i in spamList:
        hashFunc = (((a * i)+ b) % p) % n
        if B[hashFunc] == 1:
            count += 1
    return count
    
main()