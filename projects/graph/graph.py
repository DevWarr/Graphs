"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id not in self.vertices:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 not in self.vertices:
            raise KeyError(f"No vertex found with value {v1}")
        if v2 not in self.vertices:
            raise KeyError(f"No vertex found with value {v2}")
        else:
            self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices.get(vertex_id)

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        if starting_vertex not in self.vertices:
            raise KeyError(f"No vertex found with value {starting_vertex}")

        visited = {starting_vertex: True}
        q = Queue(starting_vertex)
        while len(q) > 0:
            vertex = q.dequeue()
            for v in self.get_neighbors(vertex):
                if v not in visited:
                    visited[v] = True
                    q.enqueue(v)
            print(vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        if starting_vertex not in self.vertices:
            raise KeyError(f"No vertex found with value {starting_vertex}")

        visited = {starting_vertex: True}
        s = Stack()
        s.push(starting_vertex)
        while len(s) > 0:
            vertex = s.pop()
            for v in self.get_neighbors(vertex):
                if v not in visited:
                    visited[v] = True
                    s.push(v)
            print(vertex)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if starting_vertex not in self.vertices:
            raise KeyError(f"No vertex found with value {starting_vertex}")

        if visited is None:
            visited = {starting_vertex: True}

        print(starting_vertex)
        for v in self.get_neighbors(starting_vertex):
            if v not in visited:
                visited[v] = True
                self.dft_recursive(v, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        if starting_vertex not in self.vertices:
            raise KeyError(f"No vertex found with value {starting_vertex}")
        if destination_vertex not in self.vertices:
            raise KeyError(f"No vertex found with value {destination_vertex}")

        visited = {starting_vertex: None}
        q = Queue(starting_vertex)
        while len(q) > 0:
            vertex = q.dequeue()
            for v in self.get_neighbors(vertex):

                if v == destination_vertex:
                    output = [v]
                    while vertex is not None:
                        output.append(vertex)
                        vertex = visited.get(vertex)
                    output.reverse()
                    return output

                elif v not in visited:
                    visited[v] = vertex
                    q.enqueue(v)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        if starting_vertex not in self.vertices:
            raise KeyError(f"No vertex found with value {starting_vertex}")
        if destination_vertex not in self.vertices:
            raise KeyError(f"No vertex found with value {destination_vertex}")

        visited = {starting_vertex: None}
        s = Stack()
        s.push(starting_vertex)
        while len(s) > 0:
            vertex = s.pop()
            for v in self.get_neighbors(vertex):

                if v == destination_vertex:
                    output = [v]
                    while vertex is not None:
                        output.append(vertex)
                        vertex = visited.get(vertex)
                    output.reverse()
                    return output

                if v not in visited:
                    visited[v] = vertex
                    s.push(v)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if starting_vertex not in self.vertices:
            raise KeyError(f"No vertex found with value {starting_vertex}")
        if destination_vertex not in self.vertices:
            raise KeyError(f"No vertex found with value {destination_vertex}")

        if starting_vertex == destination_vertex:
            return [starting_vertex]

        if visited is None:
            visited = {starting_vertex: None}

        for v in self.get_neighbors(starting_vertex):
            if v not in visited:
                visited[v] = True
                arr = self.dfs_recursive(v, destination_vertex, visited)
                if arr is not None:
                    return [starting_vertex, *arr]


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)
    print()

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
