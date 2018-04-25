import random
'''Creates 100 random graphs to run dijkstra's on'''

def main():
    num_nodes = random.randint(50, 10000)
    dictionary = dict()
    for i in range(num_nodes):
        bound = random.randint(2, num_nodes)
        for x in range(random.randint(1, bound) - 1, bound):
            if x == i:
                continue
            else:
                weight = random.randint(1,5)
                if i in dictionary:
                    dictionary[i].append("{},{}".format(x, weight))
                else:
                    dictionary[i] = ["{},{}".format(x, weight)]

                if x in dictionary:
                    dictionary[x].append("{},{}".format(i, weight))
                else:
                    dictionary[x] = ["{},{}".format(i, weight)]


    for key in dictionary:
        dupes = set()
        items_to_remove = []
        for item in dictionary[key]:
            if int(item[0]) not in dupes:
                dupes.add(item[0])
            else:
                items_to_remove.append(item)

        for item in items_to_remove:
            dictionary[key].remove(item)
    

    return dictionary




if __name__ == '__main__':
    for i in range(100):
        with open("fun_results_{}.txt".format(i), "w") as f:
            dictionary = main()

            for key in sorted(dictionary.keys()):
                node = str(key)
                for connected in dictionary[key]:
                    node += " " + connected
            
                f.write(node + "\n")
                
