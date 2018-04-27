import random
'''Creates 100 random graphs to run dijkstra's on'''

def main():
    num_nodes = 10 #random.randint(10, 1000)
    dictionary = {}
    dictionary_to_read = {}
    for i in range(1, num_nodes + 1): #Node
        bound = random.randint(2, num_nodes)
        for x in range(random.randint(1, bound) - 1, bound): #Node i is connected to
            #print(no_extra_paths)
            if x == i: #Prevents paths to the node itself and multiple paths to the same node
                continue
            else:
                weight = random.randint(1,8)
                if i in dictionary:
                    dictionary[i].append("{},{}".format(x, weight))
                    dictionary_to_read[i].append(" Node: {:<3} Cost: {:<3} |".format(x, weight))
                else:
                    dictionary[i] = ["{},{}".format(x, weight)]
                    dictionary_to_read[i] = [" Node: {:<3} Cost: {:<3} |".format(x, weight)]
                if x in dictionary:
                    dictionary[x].append("{},{}".format(i, weight))
                    dictionary_to_read[x].append(" Node: {:<3} Cost: {:<3} |".format(i, weight))
                else:
                    dictionary[x] = ["{},{}".format(i, weight)]
                    dictionary_to_read[x] = [" Node: {:<3} Cost: {:<3} |".format(i, weight)]

    #Gets rid of duplicates
    for key,value in dictionary.items():
        connections = set()
        correct_lyst = []
        input_lyst = []
        for i in value:
            value_prime = i.split(',')[0]
            correct_lyst.append(value_prime)
        index = 0
        for relation in value:
            if correct_lyst[index] not in connections:
                connections.add(correct_lyst[index])
                input_lyst.append(relation)
            index += 1
            
        #print(dictionary[key])
        dictionary[key] = input_lyst
        #print(dictionary[key])

    for key,value in dictionary_to_read.items():
        connections = set()
        correct_lyst = []
        input_lyst = []
        for i in value:
            value_prime = i.split(' ')[2]
            correct_lyst.append(value_prime)
        index = 0
        for relation in value:
            if correct_lyst[index] not in connections:
                connections.add(correct_lyst[index])
                input_lyst.append(relation)
            index += 1
            
        #print(dictionary[key])
        dictionary_to_read[key] = input_lyst
        #print(dictionary[key])
            
    output = []
    output.append(dictionary)
    output.append(dictionary_to_read)
    return output

if __name__ == '__main__':
    for i in range(10):
        dictionary = main()
        with open("input_{}.txt".format(i), "w") as f:
            for key in sorted(dictionary[0].keys()):
                node = "{:^3}".format(key)
                for connected in dictionary[0][key]:
                    node += " " + connected
            
                f.write(node + "\n")

        with open("input_{}_read.txt".format(i), "w") as f:
            for key in sorted(dictionary[1].keys()):
                node = "{}".format(key)
                for connected in dictionary[1][key]:
                    node += " " + connected

                f.write(node + "\n")