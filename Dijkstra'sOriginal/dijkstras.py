"""
Authors: Mark Mahan, Zackh Tucker, Taylor Cook, Tim McCoy
Group Project Code
Parallelizing Dijkstra's algorithm in Python
"""


import argparse

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
    #print(nodes)
    #Prepping for Dijkstra's Algorithm
    path_lengths = []
    X = [] #Processed vertices
    for element in nodes:
        path_lengths.append(1000000)
    path_lengths[0] = 0
    X.append('1')
    
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
    answer = ""
    for distance in path_lengths:
        if counter != len(path_lengths):
            answer += str(distance) + ","
            counter += 1
        else:
            answer += str(distance)

    print(answer)

if __name__ == "__main__":
    start = time.time()
    main()
    elapsed_time = time.time() - start
    print("Elapsed time: {}".format(elapsed_time))
