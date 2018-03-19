from Node import Node
from Graph import Graph

class DFS:

    def __init__(self, graph, start_node):
        self._graph = graph
        self._start_node = start_node
        self._nodes = []

    def run(self):
        self.__dfs(self._start_node)
        return self._nodes

    def __dfs(self, start_node):
        node_stack = [start_node]

        while(node_stack):
            node = node_stack.pop()

            if(not node.is_visited):
                node.is_visited = True
                self._nodes.append(node)
                for edge in self._graph.get_edges_for_node(node):
                    if(not edge.is_visited and edge.can_get_opposite_node(node)):
                        edge.is_visited = True
                        next_node = edge.get_opposite_node(node)
                        node_stack.append(next_node)
