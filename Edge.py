class Edge(object):
    def __init__(self, first_node, second_node, weight, is_directed):
        self._first_node = first_node
        self._second_node = second_node
        self._weight = weight
        self._is_directed = is_directed

    def get_first_node(self):
        return self._first_node

    def get_second_node(self):
        return self._second_node

    def get_weight(self):
        return self._weight

    def get_is_directed(self):
        return self._is_directed
