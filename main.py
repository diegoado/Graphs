from src.graph_base import Graph


if __name__ == "__main__":
    graph_dict = {
        "a": ["d"],
        "b": ["c"],
        "c": ["b", "c", "d", "e"],
        "d": ["a", "c"],
        "e": ["c"],
        "f": []
    }

    graph_obj = Graph(graph_dict)
    print(graph_obj)

    for node in graph_obj.vertices():
        print(graph_obj.vertex_degree(node))

    print("List of isolated vertices:")
    print(graph_obj.find_isolated_vertices())
    print("""A path from "a" to "e":""")
    print(graph_obj.find_path("a", "e"))
    print("""All patches from "a" to "e":""")
    print(graph_obj.find_all_paths("a", "e"))
    print("The maximum degree of the src is:")
    print(graph_obj.max_delta())
    print("The minimum degree of the src is:")
    print(graph_obj.min_delta())
    print("Edges:")
    print(graph_obj.edges())
    print("Degree Sequence: ")
    d_sequence = graph_obj.degree_sequence()
    print(d_sequence)

    full_filling = [[2, 2, 2, 2, 1, 1], [3, 3, 3, 3, 3, 3], [3, 3, 2, 1, 1]]
    non_full_filling = [[4, 3, 2, 2, 2, 1, 1], [6, 6, 5, 4, 4, 2, 1], [3, 3, 3, 1]]

    for sequence in full_filling + non_full_filling:
        print(sequence, Graph.erdoes_gallai(sequence))

    print("Add vertex 'z':")
    graph_obj.add_vertex("z")
    print(graph_obj)
    print("Add edge ('x','y'): ")
    graph_obj.add_edge({'x', 'y'})
    print(graph_obj)
    print("Add edge ('a','d'): ")
    graph_obj.add_edge({'a', 'd'})
    print(graph_obj)