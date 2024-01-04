import itertools as itt
import networkx as nx
import matplotlib.pyplot as plt

my_graph = nx.Graph()
with open('input') as f:
    for line in f:
        line = line.strip()
        dest, dist = line.split('=')
        destinations = dest.strip().split('to')
        destinations = [d.strip() for d in destinations]
        dist = int(dist.strip())
        my_graph.add_nodes_from(destinations)
        my_graph.add_edge(*destinations, weight = dist)

        
min_path_length = nx.path_weight(my_graph, my_graph.nodes, weight = "weight")
max_path_length = nx.path_weight(my_graph, my_graph.nodes, weight = "weight")

for path in itt.permutations(my_graph.nodes):
    min_path_length = min(min_path_length,
                          nx.path_weight(my_graph, path, weight = "weight"))
    max_path_length = max(max_path_length,
                          nx.path_weight(my_graph, path, weight = "weight"))

print('part 1 :', min_path_length)
print('part 2 :', max_path_length)
