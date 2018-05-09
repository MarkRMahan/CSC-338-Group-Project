"""
Authors: Mark Mahan, Zackh Tucker, Taylor Cook, Tim McCoy
Group Project Code
Parallelizing Dijkstra's algorithm in Python
"""
import argparse
import sys
import time
import multiprocessing as mp

dict_list = []

def dij(start, end, nodes, dict):
    for i in range(start, end):
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
        for distance in path_lengths:
            if counter != len(path_lengths):
                answer += str(counter) + ","+ str(distance) + " "
                counter += 1
            else:
                answer += str(counter)+"," +str(distance)
        #dict[i] = answer
        print(answer)

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

    num_processes = mp.cpu_count()
    each_process = (len(nodes)//num_processes) #Number of iterations each process completes
    processes = []
    leftover = (len(nodes)%num_processes)
    end = (1*2)-1
    for i in range(1, num_processes+1):
        if leftover != 0:
            if i == 1:
                start = (i*2)-1
                m = mp.Process(target = dij, args = (start, start +each_process+ 1, nodes))
                end = start+each_process+ 1
                processes.append(m)
                leftover -= 1
            else:
                m = mp.Process(target = dij, args = (end, end + each_process+1, nodes))
                end = end + each_process + 1
                processes.append(m)
                leftover -= 1
        else:
            if i == 1:
                m = mp.Process(target = dij, args = (end, end+each_process, nodes))
                end = end + each_process
                processes.append(m)
            else:
                m = mp.Process(target = dij, args = (end, end+each_process, nodes))
                end = end + each_process
                processes.append(m)


    for process in processes:
        process.start()
    for process in processes:
        process.join()

    # for i in range(1, len(nodes)+1):    #Find each node to each other node paths
    #     dij(i, nodes)

if __name__ == "__main__":
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print("Elapsed time: {}".format(elapsed_time))
