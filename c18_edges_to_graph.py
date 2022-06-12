# To get an adjacency list from a list of edges
# that shows the connection between 2 vertices,
# we have to add a new key if we've never
# seen that key before and add the adjacent
# vertex to its adjacent vertices. The same
# has to happen for the vertex we're adding,
# so that they're both in each others adjacency
# array.

edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"],
]


def edges_to_graph(edges) -> dict[str, list[str]]:
    adjacency_list: dict[str, list[str]] = {}
    for edge in edges:
        [a, b] = edge
        # If either one of the vertices is not yet
        # part of the adjacency list, add it as an index:
        if adjacency_list.get(a) == None:
            adjacency_list[a] = []
        if adjacency_list.get(b) == None:
            adjacency_list[b] = []

        if not b in adjacency_list.get(a):
            adjacency_list[a].append(b)
        if not a in adjacency_list.get(b):
            adjacency_list[b].append(a)

    return adjacency_list


print(edges_to_graph(edges))
