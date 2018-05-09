"""
Authors: Mark Mahan, Zackh Tucker, Taylor Cook, Tim McCoy
Group Project Code
Parallelizing Dijkstra's algorithm in Python
"""


<<<<<<< HEAD
import sys

graph_dict = {}

with open (sys.argv[1], 'r') as graph_doc:
    for line in graph_doc:
        values = [int(x) for x in line.replace(',', ' ').split()]
        graph_dict[values[0]] = [v for v in zip(values[1::2], values[2::2])]

#Now, here is Dijkstra's being dope
print(graph_dict)
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

print (",".join(str(l) for l in path_lengths[1:])) #print statement for the thing
=======
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
>>>>>>> ac38876552fe37855cf53727285a6197acbd729c
