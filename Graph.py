from Node import Node
from Edge import Edge

class Graph:
    def __init__(self, is_directed):
        self._nodes = {}
        self._edges = {}
        self._is_directed = is_directed

    @property
    def edges(self):
        return self._edges

    @property
    def nodes(self):
        return self._nodes

    @property
    def is_directed(self):
        return self._is_directed

    def has_node(self, node):
        return self.has_node_by_id(node.id)

    def has_node_by_id(self, node_id):
        return self._nodes.get(node_id) != None

    def get_node(self, node_id):
        return self._nodes.get(node_id)

    def add_node(self, node):
        if(not self.has_node(node)):
            self._nodes[node.id] = node

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
        if(self._edges.get(node.id) == None):
            self._edges[node.id] = [edge]
        else:
            self._edges[node.id].append(edge)

    def get_edges_for_node(self, node):
        if node.id in self._edges:
            node_edges = self._edges[node.id]
            node_edges.reverse()
            return node_edges
        else:
            return []

def main():
    first_node = Node("1")
    second_node = Node("2")
    third_node = Node("3")

    graph = Graph(False)
    graph.add_node(first_node)
    graph.add_node(second_node)
    graph.add_node(third_node)

    graph.build_edge_by_ids("1", "2", 1)
    graph.build_edge_by_ids("1", "3", 1)
    #graph.build_edge(first_node, third_node, 1)

    print(len(graph.get_edges_for_node(first_node)))
    print(len(graph.get_edges_for_node(second_node)))
    print(len(graph.get_edges_for_node(third_node)))
    #print(len(graph.get_edges().values()))


if  __name__ == "__main__": main()
