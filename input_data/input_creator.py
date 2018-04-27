import random
'''Creates 100 random graphs to run dijkstra's on'''

def main():
    num_nodes = 10 #random.randint(10, 1000)
    dictionary = {}
    dictionary_to_read = {}
    for i in range(num_nodes): #Node
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



    no_duplicates = {}
    #Gets rid of duplicates
    for key,value in dictionary.items():
        connections = set()
        print(value)
        for i in value:
            value_prime = i.split(',')[0]
            if value_prime not in connections:
                no_duplicates[key] = value
                connections.add(value_prime)

    no_duplicates_to_read = {}
    for key,value in dictionary_to_read.items():
        if value not in no_duplicates_to_read.values():
            no_duplicates_to_read[key] = value
            

    output = []
    output.append(no_duplicates)
    output.append(no_duplicates_to_read)
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
                
