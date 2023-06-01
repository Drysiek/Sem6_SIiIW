class Node:
    def __init__(self, name):
        self.name = name
        self.Edges = []

    def add_edge(self, edge):
        self.Edges.append(edge)

    def __lt__(self, other):
        return self.name < other.name
