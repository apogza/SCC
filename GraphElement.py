class GraphElement:
    def __init__(self):
        self.visited = False

    @property
    def is_visited(self):
        return self.visited

    @is_visited.setter
    def is_visited(self, val):
        self.visited = val
