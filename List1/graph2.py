from Node import Node


class Graph:
    def __init__(self):
        self.Nodes = {}

    def __int__(self, nodes):
        self.Nodes = nodes

    def add_node(self, node):
        if node not in self.Nodes:
            self.Nodes[node] = Node(node)

    def add_edge(self, edge):
        self.Nodes[edge.start_node.name].add_edge(edge)

    def neighbour_edges(self, start_node):
        for node_key, node in self.Nodes.items():
            if node.name == start_node.name:
                return node.Edges


def find_node_by_name(graph, node_name):
    for node_key, node in graph.Nodes.items():
        if node.name == node_name:
            return node
    return None


def get_coordinates(node):
    return node.Edges[0].start_stop_lat, node.Edges[0].start_stop_lon
