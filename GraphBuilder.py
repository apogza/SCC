from Node import Node
from Graph import Graph

class GraphBuilder:

    def __init__(self, file_name):
        self._file_name = file_name

    def build_graph(self):
        self._graph = Graph(False)

        file_handle = open(self._file_name, "r")
        lines = file_handle.readlines()
        file_handle.close()

        for line in lines:
            nodes = line.split(" ")
            first_node = nodes[0]
            second_node = nodes[1]

            self.__add_nodes_and_build_edge(first_node, second_node)

        return self._graph

    def __add_nodes_and_build_edge(self, first_node_id, second_node_id):
        if(not self._graph.has_node_by_id(first_node_id)):
            self._graph.add_node(Node(first_node_id))

        if(not self._graph.has_node_by_id(second_node_id)):
            self._graph.add_node(Node(second_node_id))

        self._graph.build_edge_by_ids(first_node_id, second_node_id, 1)
