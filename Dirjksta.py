import matplotlib.pyplot as plt
import  networkx as nx

class GraphDictionnaire :
    def __init__(self):
        self.graph = {}
        self.path_graph = {}
        self.G = nx.Graph()
        self.edges_labels = {}
        self.figure = plt.Figure(figsize=(5, 5), dpi=100)
        self.ax = self.figure.add_subplot(111)

    def add_sommet(self, sommet):
        if not sommet in self.graph :
            self.graph[sommet] = {}
            self.path_graph[sommet] = 100000
            self.G.add_node(sommet)

    def add_sommets(self, sommets):
        for s in sommets :
            self.add_sommet(s)

    def add_arete(self, sommet1, sommet2, weight):
        if sommet1 in self.graph and sommet2 in self.graph :
            self.graph[sommet1][sommet2] = weight
            self.graph[sommet2][sommet1] = weight
            self.G.add_edge(sommet1, sommet2, weight = weight)
            self.edges_labels[(sommet1, sommet2)] = weight

    def get_arete_weight(self, sommet1, sommet2):
        if sommet1 in self.graph and sommet2 in self.graph and self.graph.get(sommet1).get(sommet2) != None:
            return int(self.graph.get(sommet1).get(sommet2))

        else :
            return 0

    def get_all_aretes(self, sommet):
        if sommet in self.graph :
            return self.graph.get(sommet)

    def draw_garph(self, path, pathtext : str):
        self.ax.clear()

        path_edges = []
        for i in range(0, len(path) - 1):
            path_edges.append((path[i], path[i + 1]))

        other_edges = self.G.edges() - path_edges
        pos = nx.spring_layout(self.G)
        nx.draw_networkx_nodes(self.G, pos)
        nx.draw_networkx_labels(self.G, pos)
        nx.draw_networkx_edges(self.G, pos, edgelist=path_edges, edge_color='r', arrows=True)
        nx.draw_networkx_edges(self.G, pos, edgelist=other_edges, edge_color='black', arrows=True)
        nx.draw_spring(self.G, with_labels=True, font_weight='bold', ax=self.ax)
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=self.edges_labels)

        plt.suptitle(t=pathtext, fontsize=14)

        plt.show()

    def get_path(self, start, finish):
        self.path_graph[start] = 0
        queue = []
        weights = {}

        for i in self.path_graph:
            queue.append(i)
            weights[i] = 100000

        weights[start] = 0
        path = []
        predecessor = {}

        while queue :
            current_sommet = queue[0]
            aretes = self.get_all_aretes(current_sommet)
            for arete in aretes :
                if not arete in weights :
                    weights[arete] = self.get_arete_weight(current_sommet, arete) + weights[current_sommet]
                    predecessor[arete] = current_sommet


                elif (arete in weights) and (current_sommet in weights) :
                    if weights[arete] > self.get_arete_weight(current_sommet, arete) + weights[current_sommet] :
                        weights[arete] = self.get_arete_weight(current_sommet, arete) + weights[current_sommet]
                        queue.insert(0, arete)
                        queue.insert(0, current_sommet)
                        predecessor[arete] = current_sommet


            for i in range(len(weights)) :
                value = max(weights.values())
                for sommet in weights:
                    if weights[sommet] == value and sommet not in queue :
                        queue.insert(0, sommet)
            queue.remove(current_sommet)

        path.insert(0, finish)

        while path[0] != start :
            path.insert(0, predecessor[path[0]])

        self.draw_garph(pathtext=f"Le chemin le plus court entre {start} et {finish} est {path} qui coute {weights[finish]}", path=path)

        return

graphe = GraphDictionnaire()

graphe.add_sommets(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"])
graphe.add_arete("A", "B", 18)
graphe.add_arete("A", "C", 22)
graphe.add_arete("B", "C", 31)
graphe.add_arete("C", "F", 17)
graphe.add_arete("B", "E", 26)
graphe.add_arete("B", "D", 12)
graphe.add_arete("E", "F", 12)
graphe.add_arete("D", "G", 24)
graphe.add_arete("H", "G", 12)
graphe.add_arete("H", "I", 7)
graphe.add_arete("H", "K", 24)
graphe.add_arete("K", "J", 18)
graphe.add_arete("I", "J", 12)
graphe.add_arete("F", "I", 13)
graphe.add_arete("G", "E", 9)


graphe.get_path("A", "K")
