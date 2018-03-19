from GraphBuilder import GraphBuilder
from DFS import DFS

def main():
    graph_builder = GraphBuilder("SCC.txt")
    graph = graph_builder.build_graph()
    start_node = graph.get_node("1")

    dfs = DFS(graph, start_node)

    nodes = dfs.run()
    for node in nodes:
        print(node.id)

if  __name__ =='__main__':main()
