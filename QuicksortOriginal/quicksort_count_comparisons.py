#!/usr/bin/env python
#Zackh Tucker
#Nathan Hall


#+==================+==========+=========+==========+==========+==========+
#|       file       |  first   | median3 | random-1 | random-2 | random-3 |
#+==================+==========+=========+==========+==========+==========+
#| ordered-10       |       45 |      19 |       26 |       28 |       27 |
#+------------------+----------+---------+----------+----------+----------+
#| ordered-100      |     4950 |     480 |      596 |      566 |      622 |
#+------------------+----------+---------+----------+----------+----------+
#| ordered-10000    |      N/A |  113631 |   153720 |   153443 |   150094 |
#+------------------+----------+---------+----------+----------+----------+
#| randomized-10    |       20 |      20 |       21 |       24 |       39 |
#+------------------+----------+---------+----------+----------+----------+
#| randomized-100   |      667 |     538 |      622 |      729 |      608 |
#+------------------+----------+---------+----------+----------+----------+
#| randomized-10000 |   158257 |  130072 |   156028 |   155107 |   145610 |
#+------------------+----------+---------+----------+----------+----------+


import random
import sys 

A = [line.rstrip('\n') for line in open(sys.argv[1])]

for i in range(0, len(A)):       	#this for loop grabs the list and makes 
	A[i] = int(A[i])		#every item an integer
A = A[1:]

#print(A)

comparisons = 0

def partition(A, l, r):
    # set pivot to value at location A[l]
    pivot = A[l]
    # index i starts to the right of pivot
    i = l + 1
    # index j cycles through array A from the right of pivot, to the end of A
    global comparisons
    for j in range(l+1, r+1):
        comparisons += 1
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[l], A[i-1] = A[i-1], A[l]
    return i-1

def quicksort_first(A, l, r):
    if l >= r:
        return
        
    pivot_index = partition(A, l, r)
    quicksort_first(A, l, pivot_index-1)
    quicksort_first(A, pivot_index+1, r)


def quicksort_median3(A, l , r):
    if l>= r:
        return
    
    x, y, z = A[l], A[int((l+r)/2)], A[r]
    
    # if x is the median value
    if (y < x and x < z) or (z < x and x < y):
        median_l = l
    # if y is the median value
    elif (x < y and y < z) or (z < y and y < x):
        median_l = int((l+r)/2)
    # if z is the median value
    else:
        median_l = r
    
    A[l], A[median_l] = A[median_l], A[l]
    pivot_index = partition(A, l, r)
    quicksort_median3(A, l, pivot_index-1)
    quicksort_median3(A, pivot_index+1, r)

def quicksort_random(A, l, r):
    if l >= r:
        return
        
    random_l = random.randint(l, r)
    
    A[l], A[random_l] = A[random_l], A[l]
    pivot_index = partition(A, l, r)
    quicksort_random(A, l, pivot_index-1)
    quicksort_random(A, pivot_index+1, r)


#A = [4,3,2,5,6,1]
#random.shuffle(A)

#quicksort_random(A, 0, len(A)-1)
#print(A)

if sys.argv[2] == "first":
    quicksort_first(A, 0, len(A)-1)
    print(comparisons)

if sys.argv[2] == "median3":
    quicksort_median3(A, 0, len(A)-1)
    print(comparisons)
    
if sys.argv[2] == "random":
    quicksort_random(A, 0, len(A)-1)
    print(comparisons)













