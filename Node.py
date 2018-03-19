from GraphElement import GraphElement

class Node(GraphElement):
    def __init__(self, node_id):
        #super(GraphElement, self)
        self._id = node_id
        self.visited = False

    @property
    def id(self):
        return self._id
