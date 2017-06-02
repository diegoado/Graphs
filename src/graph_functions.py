def null_graph ():
    return {}

def vertices(graph):
    """ returns the vertices of a src """
    return graph.keys()

def edges(graph):
    """ returns the edges of a src """
    edges = []
    for vertex in graph:
        for neighbour in graph[vertex]:
            if {neighbour, vertex} not in edges:
                edges.append({vertex, neighbour})
    return edges
    
def add_vertex(graph, vertex):
    """ If the vertex "vertex" is not in 
        self.__graph_dict, a key "vertex" with an empty
        list as a value is added to the dictionary. 
        Otherwise nothing has to be done. 
    """
    if vertex not in graph:
        graph[vertex] = []

def add_edge(graph, edge):
    """ assumes that edge is of type set, tuple or list; 
        between two vertices can be multiple edges!
    """
    edge = set(edge)
    vertex1 = edge.pop();
    if not edge:
        vertex2=vertex1
    else: vertex2 = edge.pop()
    if vertex1 in vertices(graph) and vertex2 in vertices(graph):
        graph[vertex1].append(vertex2)
        if vertex1 != vertex2:
            graph[vertex2].append(vertex1)       
    
def print_graph (graph):
    res = "vertices: "
    for k in graph:
        res += str(k) + " "
    res += "\n edges: "
    for edge in edges(graph):
        res += str(edge) + " "
    return res

def find_isolated_vertices(graph):
        """ returns a list of isolated vertices. """
        isolated = []
        for vertex in graph:
            if not graph[vertex]:
                isolated += [vertex]
        return isolated

def vertex_degree(vertex,graph):
    """ The degree of a vertex is the number of edges connecting
        it, i.e. the number of adjacent vertices. Loops are counted 
        double, i.e. every occurence of vertex in the list 
        of adjacent vertices. """ 
    adj_vertices =  graph[vertex]
    degree = len(adj_vertices) + adj_vertices.count(vertex)
    return degree

def Delta(graph):
    """ the maximum degree of the vertices """
    max = 0
    for vertex in graph:
        vd = vertex_degree(vertex,graph)
        if vd > max:
            max = vd
    return max


if __name__ == "__main__":
    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }




