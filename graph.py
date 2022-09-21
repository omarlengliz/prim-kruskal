from typing import List, Union
from read import readg,lengthg
import numpy as np
class UndirectedGraph:
    def __init__(self, num_vertices: int):
        """Initializing the member variables of the graph instance."""
        self.graph: List[List] = []
        self.num_vertices: int = num_vertices

    def add_link(
        self, vertex_one: Union[int, float, str],
        vertex_two: Union[int, float, str],
        weight: int
    ):
        """
        This will add a link from vertex_one to vertex_two.
        The graph representation will be in the form of an edge list.
        """
        self.graph.append([vertex_one, vertex_two, weight])

    def find_parent(
        self, parent: List[int],
        vertex: int
    ):
        """This function will find the parent of a vertex."""
        if parent[vertex] == vertex:
            return vertex
        return self.find_parent(parent, parent[vertex])

    def union(
        self, parent: List,
        rank: List,
        node_one: int,
        node_two: int
    ):
        vertex_one = self.find_parent(parent, node_one)
        vertex_two = self.find_parent(parent, node_two)
        if rank[vertex_one] < rank[vertex_two]:
            parent[vertex_one] = vertex_two
        elif rank[vertex_one] > rank[vertex_two]:
            parent[vertex_two] = vertex_one
        else:
            parent[vertex_two] = vertex_one
            rank[vertex_one] += 1

    def print_min_spanning_tree(self, tree: List[List]):
        total_cost: int
        total_cost = 0
        t=np.zeros([lengthg(),lengthg()])
        for vertex_one, vertex_two, weight in tree:
            t[vertex_one,vertex_two]=weight
            print(f"{vertex_one} - {vertex_two}  |  {weight}")
            total_cost += weight
        print(f"Total cost of minimum spanning tree: {total_cost}")
        return t,total_cost
    def kruskal_min_spanning_tree(self) -> List[List]:
        minimum_spanning_tree: List[List]
        graph_sorted_by_weights: List[List]
        rank: List[int]
        minimum_spanning_tree = []
        graph_sorted_by_weights = sorted(self.graph,
                                         key=lambda element: element[2])
        rank = [0] * self.num_vertices
        parent = [num for num in range(self.num_vertices)]
        for vertex_one, vertex_two, weight in graph_sorted_by_weights:
            vertex_one_parent = self.find_parent(parent, vertex_one)
            vertex_two_parent = self.find_parent(parent, vertex_two)
            if vertex_one_parent != vertex_two_parent:
                minimum_spanning_tree.append([vertex_one, vertex_two, weight])
                self.union(parent, rank, vertex_one_parent, vertex_two_parent)
        return minimum_spanning_tree

    def prim_min_spanning_tree(self):
        visited: List = [0]
        minimum_spanning_tree: List = []

        while len(visited) != len({i[1] for i in self.graph}):
            valid_edges = self.get_valid_edges(visited)
            smallest_edge = min(valid_edges, key=lambda l: l[2])
            minimum_spanning_tree.append(smallest_edge)
            visited.append(smallest_edge[1])
        return minimum_spanning_tree

    def get_valid_edges(self, visited: List) -> List:
        return [
            edges for edges in self.graph
            if edges[0] in visited and edges[1] not in visited
        ]

def graphini():
    graph=UndirectedGraph(lengthg())
    l=readg()
    for i in range(lengthg()):
        for j in range(lengthg()):
            if(l[i][j]!=0):
                graph.add_link(i,j,l[i][j])
    return graph
def kruskal():
    return graphini().print_min_spanning_tree(graphini().kruskal_min_spanning_tree())

def prim():
    return graphini().print_min_spanning_tree(graphini().prim_min_spanning_tree())

