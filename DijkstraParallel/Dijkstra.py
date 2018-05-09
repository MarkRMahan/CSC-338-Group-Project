"""
Authors: Mark Mahan, Zackh Tucker, Taylor Cook, Tim McCoy
Group Project Code
Parallelizing Dijkstra's algorithm in Python
"""
import argparse
import sys
import random
import time
import statistics as stats
import multiprocessing as mp
import os.path

#q = mp.Queue()

def dij(i, nodes):
    #Prepping for Dijkstra's Algorithm
    path_lengths = []
    X = [] #Processed vertices
    for element in nodes:
        path_lengths.append(1000000)
    path_lengths[i-1] = 0 #Set the starting node -> starting node to 0
    X.append(str(i))

    #Dijkstra's Magical Algorithm
    while len(X) < len(path_lengths):
        for reached_node in X:
            for edge in nodes[reached_node]:
                candidate = path_lengths[int(reached_node) - 1] + int(edge[-1])
                if candidate < path_lengths[int(edge[0]) - 1] or edge[0] not in X:
                    X.append(edge[0])
                    path_lengths[int(edge[0]) - 1] = candidate

    #Used to get the output in the correct format
    counter = 1
    answer = "{}\t".format(i)
    f = open('dij_serial{}.txt'.format(len(nodes)), 'a')
    f.write(str(i)+"\n")
    for distance in path_lengths:
        f.write(str(counter) + ","+ str(distance) + "\n")
        if counter != len(path_lengths):
            answer += str(counter) + ","+ str(distance) + " "
            counter += 1
        else:
            answer += str(counter)+"," +str(distance)
    f.write("~ ~ ~ ~\n")
    f.close()

def main():
    arg_parser = argparse.ArgumentParser(description='Print the given input file.')
    arg_parser.add_argument('filename', help='path to a file')
    elements = arg_parser.parse_args()
    with open(elements.filename, 'r') as file:
        file_input = file.readlines() #Input
    nodes = {}
    for index in file_input:
        #Puts the file's contents into the nodes dictionary
        nodes[index.split()[0]] = []
        for element in index.split():
            if index.split()[0] != element:
                nodes[index.split()[0]].append(element.split(","))
    if os.path.exists('dij_serial{}.txt'.format(len(nodes))):
        os.remove('dij_serial{}.txt'.format(len(nodes)))
    for i in range(1, len(nodes)+1):    #Find each node to each other node paths
        dij(i, nodes)

if __name__ == "__main__":
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print("Elapsed time: {}".format(elapsed_time))
