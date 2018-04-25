import random
'''Creates 100 random graphs to run dijkstra's on'''

def main():
    num_nodes = random.randint(10, 30)
    dictionary = {}
    for i in range(num_nodes):
        bound = random.randint(2, num_nodes)
        for x in range(random.randint(1, bound) - 1, bound):
            if x == i: # Prevents paths to the node itself
                continue
            else:
                weight = random.randint(1,5)
                if i in dictionary:
                    dictionary[i].append(" Node: {:<3} Cost: {:<3} |".format(x, weight))
                else:
                    dictionary[i] = [" Node: {:<3} Cost: {:<3} |".format(x, weight)]

                if x in dictionary:
                    dictionary[x].append(" Node: {:<3} Cost: {:<3} |".format(i, weight))
                else:
                    dictionary[x] = [" Node: {:<3} Cost: {:<3} |".format(i, weight)]


    no_duplicates = {}
    #Gets rid of duplicates
    for key,value in dictionary.items():
        if key not in no_duplicates.keys():
            no_duplicates[key] = value
    
    return no_duplicates




if __name__ == '__main__':
    for i in range(10):
        with open("input_{}.txt".format(i), "w") as f:
            dictionary = main()

            for key in sorted(dictionary.keys()):
                node = "{:^3}".format(key)
                for connected in dictionary[key]:
                    node += " " + connected
            
                f.write(node + "\n")
                
