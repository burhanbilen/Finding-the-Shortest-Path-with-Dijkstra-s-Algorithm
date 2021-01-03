from collections import defaultdict, deque
import matplotlib.pyplot as plt
import numpy as np

first = 'Kocaeli'
last = "Konya"

coords = {"Kocaeli":[121,319],"Yalova":[168,320], "Bursa":[217,272], "Balıkesir":[291,175], "Manisa":[417,155], 
          "Uşak":[400,315], "Afyonkarahisar":[388,412], "Kütahya":[316,366], "Eskişehir":[270,415],
          "İnegöl":[248,364], "Sakarya":[153,401], "Düzce":[144,474], "Bolu":[154,514], "Ankara":[250,626],
          "Polatlı":[291,562], "Kırıkkale":[262,685], "Konya":[488,596]}


fig, ax = plt.subplots()

def PLOT():
    plt.plot([coords["Kocaeli"][0],coords["Yalova"][0]],[coords["Kocaeli"][1],coords["Yalova"][1]], "gray")
    plt.plot([coords["Kocaeli"][0],coords["Sakarya"][0]],[coords["Kocaeli"][1],coords["Sakarya"][1]], "gray")
    plt.plot([coords["Yalova"][0],coords["Bursa"][0]],[coords["Yalova"][1],coords["Bursa"][1]], "gray")
    plt.plot([coords["Bursa"][0],coords["İnegöl"][0]],[coords["Bursa"][1],coords["İnegöl"][1]], "gray")
    plt.plot([coords["Bursa"][0],coords["Balıkesir"][0]],[coords["Bursa"][1],coords["Balıkesir"][1]], "gray")
    plt.plot([coords["Balıkesir"][0],coords["Manisa"][0]],[coords["Balıkesir"][1],coords["Manisa"][1]], "gray")
    plt.plot([coords["Manisa"][0],coords["Uşak"][0]],[coords["Manisa"][1],coords["Uşak"][1]], "gray")
    plt.plot([coords["Uşak"][0],coords["Afyonkarahisar"][0]],[coords["Uşak"][1],coords["Afyonkarahisar"][1]], "gray")
    plt.plot([coords["Afyonkarahisar"][0],coords["Konya"][0]],[coords["Afyonkarahisar"][1],coords["Konya"][1]], "gray")
    plt.plot([coords["Kütahya"][0],coords["Uşak"][0]],[coords["Kütahya"][1],coords["Uşak"][1]], "gray")
    plt.plot([coords["Kütahya"][0],coords["Afyonkarahisar"][0]],[coords["Kütahya"][1],coords["Afyonkarahisar"][1]], "gray")
    plt.plot([coords["İnegöl"][0],coords["Eskişehir"][0]],[coords["İnegöl"][1],coords["Eskişehir"][1]], "gray")
    plt.plot([coords["Polatlı"][0],coords["Ankara"][0]],[coords["Polatlı"][1],coords["Ankara"][1]], "gray")
    plt.plot([coords["Polatlı"][0],coords["Afyonkarahisar"][0]],[coords["Polatlı"][1],coords["Afyonkarahisar"][1]], "gray")
    plt.plot([coords["Ankara"][0],coords["Kırıkkale"][0]],[coords["Ankara"][1],coords["Kırıkkale"][1]], "gray")
    plt.plot([coords["Sakarya"][0],coords["Düzce"][0]],[coords["Sakarya"][1],coords["Düzce"][1]], "gray")
    plt.plot([coords["Ankara"][0],coords["Kırıkkale"][0]],[coords["Ankara"][1],coords["Kırıkkale"][1]], "gray")
    plt.plot([coords["Düzce"][0],coords["Bolu"][0]],[coords["Düzce"][1],coords["Bolu"][1]], "gray")
    plt.plot([coords["Eskişehir"][0],coords["Polatlı"][0]],[coords["Eskişehir"][1],coords["Polatlı"][1]], "gray")
    plt.plot([coords["Sakarya"][0],coords["İnegöl"][0]],[coords["Sakarya"][1],coords["İnegöl"][1]], "gray")
    plt.plot([coords["Sakarya"][0],coords["Eskişehir"][0]],[coords["Sakarya"][1],coords["Eskişehir"][1]], "gray")
    plt.plot([coords["Ankara"][0],coords["Konya"][0]],[coords["Ankara"][1],coords["Konya"][1]], "gray")
    plt.plot([coords["Kırıkkale"][0],coords["Konya"][0]],[coords["Kırıkkale"][1],coords["Konya"][1]], "gray")
    plt.plot([coords["Bolu"][0],coords["Ankara"][0]],[coords["Bolu"][1],coords["Ankara"][1]], "gray")
    plt.plot([coords["Eskişehir"][0],coords["Kütahya"][0]],[coords["Eskişehir"][1],coords["Kütahya"][1]], "gray")
    plt.xlabel("X - Axis")
    plt.ylabel("Y - Axis")
    
def SCTR():
    x = []
    y = []
    for i in coords.values():
        x.append(i[0])
        y.append(i[1])
    x = np.array(x)
    y = np.array(y)
    ax.scatter(x, y)
    n = [i for i in coords.keys()]
    for i, j in enumerate(n):
        ax.annotate(j, (x[i], y[i]), color = "black")

SCTR()
PLOT()
plt.show()
    
class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)
    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            try:
                weight = current_weight + graph.distances[(min_node, edge)]
            except:
                continue
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node
    return visited, path

def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)

if __name__ == '__main__':
    g = Graph()
    
    for node in coords.keys():
        g.add_node(node)

    g.add_edge('Kocaeli', 'Yalova', 38.1)
    g.add_edge('Kocaeli', 'Sakarya', 98.9)
    g.add_edge('Yalova', 'Bursa', 71)
    g.add_edge('Sakarya', 'İnegöl', 136)
    g.add_edge('Sakarya', 'Eskişehir', 184)
    g.add_edge('Sakarya', 'Düzce', 83.9)
    g.add_edge('Bursa', 'İnegöl', 46.8)
    g.add_edge('Bursa', 'Balıkesir', 147)
    g.add_edge('İnegöl', 'Eskişehir', 107)
    g.add_edge('Eskişehir', 'Kütahya', 78.7)
    g.add_edge('Eskişehir', 'Polatlı', 157)
    g.add_edge('Balıkesir', 'Manisa', 142)
    g.add_edge('Manisa', 'Uşak', 194)
    g.add_edge('Uşak', 'Afyonkarahisar', 111)
    g.add_edge('Kütahya', 'Uşak', 142)
    g.add_edge('Kütahya', 'Afyonkarahisar', 96.5)
    g.add_edge('Afyonkarahisar', 'Konya', 227)
    g.add_edge('Düzce', 'Bolu', 50.5)
    g.add_edge('Bolu', 'Ankara', 187)
    g.add_edge('Ankara', 'Kırıkkale', 78.6)
    g.add_edge('Ankara', 'Konya', 261)
    g.add_edge('Polatlı', 'Ankara', 80.9)
    g.add_edge('Polatlı', 'Afyonkarahisar', 183)
    g.add_edge('Kırıkkale', 'Konya', 251)

shortest_coords = []
shortest_city = []
for i in shortest_path(g, first, last)[1]:
    shortest_coords.append(coords[i])
    shortest_city.append(i)

i = 0
bigram = []
while True:
    if len(bigram) == len(shortest_coords)-1:
        break
    else:
        bigram.append([shortest_coords[i], shortest_coords[i+1]])
    i += 1

def SCTR_shortest():
    x = [i[0] for i in shortest_coords]
    y = [j[1] for j in shortest_coords]
    plt.scatter(x, y)
    n = [k for k in shortest_city]
    for i, j in enumerate(n):
        plt.annotate(j, (x[i], y[i]), color = "black")

PLOT()
SCTR_shortest()

for i in bigram:
    plt.plot([i[0][0],i[1][0]],[i[0][1],i[1][1]], "red")

plt.title(f"Shortest Path's Length: {round(shortest_path(g, first, last)[0], 1)} KM")
plt.xlabel("X - Axis")
plt.ylabel("Y - Axis")
plt.show()
