class WeightedGraphVertex:
    '''A vertex is the same as a node and used to construct a graph.'''

    def __init__(self, value: str) -> None:
        '''Initialize a vertex with a string as its value.

        Parameters
        ----------
        value : str
            Assign the vertex a basic string as its value.

        Returns
        -------
        None

        '''
        self.value: str = value
        # Instead of using an array to store the adjacent
        # vertices, we're now going to use a hasp map:
        self.adjacent_vertices: dict[WeightedGraphVertex, int] = {}

    # For using 'Vertex' as a type within one of its class,
    # methods, we have to pass it as an argument:
    def add_adjacent_vertex(self, vertex: 'WeightedGraphVertex', weight: int) -> None:
        '''Append a vertex to the list of adjacent vertices.

        Examples
        --------
        If we init a vertex with `alice = Vertex("Alice")` and then
        add Bob as an adjacent node, like `alice.add_adjacent_vertex(bob, 12)`,
        `bob` will be in Alice' dict of adjacent nodes, whilst `alice`
        is found in Bob's list of adjacent nodes. We've also assigned an integer
        value of 12 to the edge between them.

        Parameters
        ----------
        vertex : Vertex
            The vertex to be appended to the list of adj. vertices.

        weight : int
            The weight that is assigned to the edge between the two vertices.

        Returns
        -------
        None

        '''
        # If the vertex is already in the dict of
        # adjacent vertices, just return. This makes sure to
        # not end up in an infinite loop, once they've been added
        # to each others adjacent vertices list:
        if self.adjacent_vertices.get(vertex):
            return
        # Add the vertex to the hash map of adjacent vertices by
        # adding it as a key with the weight as the value to the dict:
        self.adjacent_vertices[vertex] = weight
        # Compared to the regular vertex graph, we don't want
        # want to the call the function from the POV of the vertex
        # we pass. That is because we'd like to asign different values
        # to the edges in some instances.


boston = WeightedGraphVertex("Boston")
atlanta = WeightedGraphVertex("Atlanta")
chicago = WeightedGraphVertex("Chicago")
denver = WeightedGraphVertex("Denver")
elpaso = WeightedGraphVertex("El Paso")

boston.add_adjacent_vertex(denver, 180)
boston.add_adjacent_vertex(chicago, 120)

atlanta.add_adjacent_vertex(denver, 160)
atlanta.add_adjacent_vertex(boston, 100)

chicago.add_adjacent_vertex(elpaso, 80)

denver.add_adjacent_vertex(chicago, 40)
denver.add_adjacent_vertex(elpaso, 140)

elpaso.add_adjacent_vertex(boston, 100)


