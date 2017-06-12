class Graph(object):
    def __init__(self, graph_dict=None):
        """ Initializes a src object, 
            if no dictionary or None is given, an empty dictionary will be used
        """
        self.__graph_dict = graph_dict if graph_dict else {}

    @property
    def graph_dict(self):
        return self.__graph_dict

    def vertices(self):
        """ Returns the vertices of a src """
        return self.__graph_dict.keys()

    def edges(self):
        """ Returns the edges of a src """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary. Otherwise nothing has to be done. 
        """
        if vertex not in self.vertices():
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        """ Assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        u = edge.pop()
        if edge:
            # not a loop
            v = edge.pop()
        else:
            # a loop
            v = u
        if u in self.vertices():
            self.__graph_dict[u].append(v)
        else:
            self.__graph_dict[u] = [v]

    def __generate_edges(self):
        """ A static method generating the edges of the src "src". 
            Edges are represented as sets with one (a loop back to the vertex) or two 
            vertices 
        """
        edges = []
        for vertex in self.vertices():
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})

        return edges

    def find_isolated_vertices(self):
        """ Returns a list of isolated vertices
        """
        isolated = []
        graph = self.__graph_dict.copy()

        for vertex in graph:
            if not graph[vertex]:
                isolated.append(vertex)

        return isolated

    def find_path(self, start_vertex, end_vertex, path=None):
        """ Find a path from start_vertex to end_vertex in src
        """
        if not path:
            path = []

        path.append(start_vertex)
        graph = self.__graph_dict.copy()

        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None

        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path: 
                    return extended_path

        return None

    def find_all_paths(self, start_vertex, end_vertex, path=None):
        """ Find all paths from start_vertex to end_vertex in src
        """
        if not path:
            path = []

        path.append(start_vertex)
        graph = self.__graph_dict.copy()

        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []

        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path)
                for p in extended_paths: 
                    paths.append(p)

        return paths

    def is_connected(self, vertices_encountered=None, start_vertex=None):
        """ Determines if the src is connected """
        if vertices_encountered is None:
            vertices_encountered = set()

        graph = self.__graph_dict.copy()
        vertices = graph.keys()

        if not start_vertex:
            # Choose a vertex from src as a starting point
            start_vertex = vertices[0]

        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in graph[start_vertex]:
                if vertex not in vertices_encountered:
                    if self.is_connected(vertices_encountered, vertex):
                        return True
        else:
            return True

        return False

    def vertex_degree(self, vertex):
        """ The degree of a vertex is the number of edges connecting it,
            i.e. the number of adjacent vertices. Loops are counted double,
            i.e. every occurrence of vertex in the list of adjacent vertices
        """
        adj_vertices = self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)
        return degree

    def degree_sequence(self):
        """ Calculates the degree sequence
        """
        seq = []
        for vertex in self.vertices():
            seq.append(self.vertex_degree(vertex))

        seq.sort(reverse=True)
        return tuple(seq)

    def min_delta(self):
        """ The minimum degree of the vertices
        """
        curr_min = float('inf')
        for vertex in self.vertices():
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree < curr_min:
                curr_min = vertex_degree

        return curr_min

    def max_delta(self):
        """ The maximum degree of the vertices
        """
        curr_max = float('-inf')
        for vertex in self.vertices():
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > curr_max:
                curr_max = vertex_degree

        return curr_max

    def density(self):
        """ Method to calculate the density of a src
        """
        graph = self.__graph_dict.copy()
        vertexes = len(graph.keys())
        edges = len(self.edges())

        return 2.0 * edges / (vertexes *(vertexes - 1))

    def diameter(self):
        """ Calculates the diameter of the src
        """
        vertexes = self.vertices()
        pairs = [(vertexes[i],vertexes[j])
                 for i in range(len(vertexes) - 1) for j in range(i + 1, len(vertexes))]

        smallest_paths = []
        for (s,e) in pairs:
            paths = self.find_all_paths(s,e)
            smallest = sorted(paths, key=len)[0]
            smallest_paths.append(smallest)

        smallest_paths.sort(key=len)
        # longest path is at the end of list, 
        # i.e. diameter corresponds to the length of this path
        diameter = len(smallest_paths[-1])
        return diameter

    @staticmethod
    def is_degree_sequence(degree_sequence):
        """ Method returns True, if the sequence "sequence" is a 
            degree sequence, i.e. a non-increasing sequence. 
            Otherwise False is returned.
        """
        # Check if the sequence sequence is non-increasing:
        return all(x >= y for x, y in zip(degree_sequence, degree_sequence[1:]))

    @staticmethod
    def erdoes_gallai(degree_sequence):
        """ Checks if the condition of the Erdoes-Gallai inequality 
            is full filled
        """
        if sum(degree_sequence) % 2:
            # sum of sequence is odd
            return False
        if Graph.is_degree_sequence(degree_sequence):
            for k in range(1, len(degree_sequence) + 1):
                left = sum(degree_sequence[:k])
                right = k * (k - 1) + sum([min(x,k) for x in degree_sequence[k:]])
                if left > right:
                    return False
        else:
            # sequence is increasing
            return False

        return True

    def __str__(self):
        str_graph = "vertices: "
        for k in self.vertices():
            str_graph += str(k) + " "

        str_graph += "\nedges: "
        for edge in self.__generate_edges():
            str_graph += str(edge) + " "

        return str_graph
