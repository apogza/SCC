from Node import Node
from Edge import Edge

class Graph(object):
    def __init__(self, is_directed):
        self._nodes = {}
        self._edges = {}
        self._is_directed = is_directed

    def has_node(self, node):
        return self._nodes.get(node.get_id()) != None

    def get_node(self, node_id):
        return self._nodes.get(node_id)

    def add_node(self, node):
        if(not self.has_node(node)):
            self._nodes[node.get_id()] = node

    def build_edge(self, first_node, second_node, weight):
        if(not self.has_node(first_node) or not self.has_node(second_node)):
            raise ValueError("One of the given nodes is not part of this graph")

        edge = Edge(first_node, second_node, weight, self._is_directed)
        self.__add_edge_for_node(first_node, edge)

        if(not self._is_directed):
            self.__add_edge_for_node(second_node, edge)

    def build_edge_by_ids(self, first_node_id, second_node_id, weight):
        first_node = self._nodes.get(first_node_id)
        second_node = self._nodes.get(second_node_id)

        if(first_node == None or second_node == None):
            raise ValueError("One of the given nodes is not part of this graph")

        self.build_edge(first_node, second_node, weight)

    def __add_edge_for_node(self, node, edge):
        if(self._edges.get(node.get_id()) == None):
            self._edges[node.get_id()] = [edge]
        else:
            self._edges[node.get_id()].append(edge)

    def get_edges_for_node(self, node):
        return self._edges[node.get_id()]

    def get_edges(self):
        return self._edges

    def get_nodes(self):
        return self._nodes

first_node = Node("1")
second_node = Node("2")
third_node = Node("3")

graph = Graph(False)
graph.add_node(first_node)
graph.add_node(second_node)
graph.add_node(third_node)

graph.build_edge(first_node, second_node, 1)
graph.build_edge_by_ids("1", "3", 1)

print(len(graph.get_edges_for_node(first_node)))
print(len(graph.get_edges_for_node(second_node)))
print(len(graph.get_edges_for_node(third_node)))
