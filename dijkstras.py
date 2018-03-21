#!/usr/bin/env python

"""
Authors: Zackh Tucker, Nate Hall
Assignment: HW5 - Implementing Dijkstra's in python

Question 1:     
        Running Dijkstra's recursively on every node in the graph as the base
        
Question 2: 
    O(nlgn) 
    More exact running time, not including reading in the file would be
    T(nlgn + bunch of constants)

"""

import sys

graph_dict = {}

with open (sys.argv[1], 'r') as graph_doc:
    for line in graph_doc:
        values = [int(x) for x in line.replace(',', ' ').split()]
        graph_dict[values[0]] = [v for v in zip(values[1::2], values[2::2])]

#for a in graph_dict:
#    print a, ":", graph_dict[a]
#    
#Now, here is Dijkstra's being dope

visited_nodes = [1] #initializing visited array - c

num_nodes = len(graph_dict) #making variable for length of dictionary - c

path_lengths = [-1, 0] + [1000000] * (num_nodes - 1) #initializing lengths array, node 0 doesn't exist so it's -1, node 1 is where we start, so it's 0, all other nodes are intialized to 1,000,000

while len(visited_nodes) < num_nodes: # - n
    potential_edges = [] #empty list for potential edges to be checked    - c
 
    #going through all of the visited nodes
    for vertex in visited_nodes: #this whole loop will be around log n I believe 
        for w, l in graph_dict[vertex]: #looking at data points for each vertex
            if w not in visited_nodes: #going through all of the not visited nodes
                potential_edges.append((w, path_lengths[vertex] + l)) #add node to potential_edges to be checked     
    star = min(potential_edges, key=lambda n: n[1])#function to find the min
            
    visited_nodes.append(star[0]) #add the edge to visited to start the loop over - c
            
    path_lengths[star[0]] = star[1] #setting up to find the new value for the next iteration - c
            
print ",".join(str(l) for l in path_lengths[1:]) #print statement for the thing