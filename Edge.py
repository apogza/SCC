from GraphElement import GraphElement

class Edge(GraphElement):
    def __init__(self, first_node, second_node, weight, is_directed):
        self._first_node = first_node
        self._second_node = second_node
        self._weight = weight
        self._is_directed = is_directed
        self.visited = False

    @property
    def first_node(self):
        return self._first_node

    @property
    def second_node(self):
        return self._second_node

    @property
    def weight(self):
        return self._weight

    @property
    def is_directed(self):
        return self._is_directed

    def can_get_opposite_node(self, node):
        if(node == self.first_node):
            return self.second_node

        if(node == self.second_node and not self.is_directed):
            return self.first_node

        raise ValueError("Cannot go against the direction of the edge")

    def get_opposite_node(self, node):
        if(self.can_get_opposite_node(node)):
            return self.second_node if node == self.first_node else self.first_node

        raise ValueError("Cannot go against the direction of the edge")
