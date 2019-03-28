#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def updateAdjusted (adj, skipper, increment, skippers):
    # determine the numbers to skip based on indicies in adj
    allreadyIncremented  = []
    # list of indicies to be replaced, eg [(5: 4)] is derived from 4 being in the spot
    # of 5
    replacedIndicies = {}
    for i in adj.keys():
        replacedIndicies.update({i + adj.get(i) : i })
    while increment > 0:
        offset = increment
        notFound = True
        numberToBeChecked = skipper - offset
        while notFound and numberToBeChecked > 0:
            if numberToBeChecked not in replacedIndicies.keys() and (numberToBeChecked in allreadyIncremented or numberToBeChecked in skippers):
                offset += 1
                numberToBeChecked = skipper - offset
            elif numberToBeChecked in replacedIndicies.keys():
                numberToBeChecked = replacedIndicies.get(numberToBeChecked)
                notFound = False
            else:
                notFound = False
        if numberToBeChecked  not in adj.keys():
            adj.update({numberToBeChecked: 1})
            allreadyIncremented.append(numberToBeChecked)
        else:
            adj.update({numberToBeChecked : adj.get(numberToBeChecked) + 1 })
            allreadyIncremented.append(numberToBeChecked)
        increment -= 1
    return adj

def minimumBribes(q):
    counter = 0
    isChaotic = False
    adjusted = {}
    skippers = []
    for i in range(len(q)):
        isInAdjusted = q[i] in adjusted.keys()
        offset = adjusted.get(q[i]) - 1 if isInAdjusted else - 1
        expectedIndex = q[i] + offset
        if i == expectedIndex -1:
            counter += 1
            skippers.append(q[i])
            adjusted = updateAdjusted(adjusted, q[i], 1, skippers)
        elif i == expectedIndex - 2:
            counter += 2
            skippers.append(q[i])
            adjusted = updateAdjusted(adjusted, q[i], 2, skippers)
        elif i < expectedIndex - 2:
            isChaotic = True
    print 'Too chaotic' if isChaotic else counter
    pass


if __name__ == '__main__':
    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        q = map(int, raw_input().rstrip().split())

        minimumBribes(q)
