class Vertex:
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
        self.adjacent_vertices: list[Vertex] = []

    # For using 'Vertex' as a type within one of its class,
    # methods, we have to pass it as an argument:
    def add_adjacent_vertex(self, vertex: 'Vertex') -> None:
        '''Append a vertex to the list of adjacent vertices.

        This method will both add the vertex we pass as an argument
        to the one we're calling the method from, but also add the
        vertex we're calling the method from to the vertex we pass
        as an argument.

        Examples
        --------
        If we init a vertex with `alice = Vertex("Alice")` and then
        add Bob as an adjacent node, like `alice.add_adjacent_vertex(bob)`,
        `bob` will be in Alice' list of adjacent nodes, whilst `alice`
        is found in Bob's list of adjacent node.

        Parameters
        ----------
        vertex : Vertex
            The vertex to be appended to the list of adj. vertices.

        Returns
        -------
        None

        '''
        # If the vertex is already in the list of
        # adjacent vertices, just return. This makes sure to
        # not end up in an infinite loop, once they've been added
        # to each others adjacent vertices list:
        if vertex in self.adjacent_vertices:
            return
        # Add the vertex to the list of adjacent vertices:
        self.adjacent_vertices.append(vertex)
        # When we call the function on Alice for example
        # and pass Bob as an argument, we add Alice as
        # an adjacent vertex (self) to the vertex we pass
        # into the function (Bob in this example). This way
        # they share each other as adjacent vertices:
        vertex.add_adjacent_vertex(self)


def dfs(vertex: Vertex, visited_vertices: dict[str, bool] = {}):
    '''Perform depth-first search on a vertex, which may be part of a graph.

    Parameters
    ----------
    vertex : Vertex
        The vertex from which we're starting the DFS.

    visited_vertices : dict[str, bool]
        This (optional) dict helps us keep track of all the vertices 
        we've visited so far. It's initialized as an empty dict that 
        saves the value of vertex as its key and True as the value of 
        that key. Because it's passed down each function call, the key
        is added to same object in memory every time.

    '''
    # Add the vertex we pass as an argument to the dictionary,
    # because the first time we perform DFS on that vertex, it's
    # not going to be in the dict yet:
    visited_vertices[vertex.value] = True
    print(vertex.value)

    for adjacent_vertex in vertex.adjacent_vertices:
        if visited_vertices.get(adjacent_vertex.value):
            # If we can find the value inside our hash table,
            # we have to continue on with the next adjacent vertex,
            # because return would just end the DFS on that vertex.
            continue

        dfs(adjacent_vertex, visited_vertices)


def dfs_val(vertex: Vertex, search_val: str, visited_vertices: dict[str, bool] = {}) -> None | Vertex:
    '''Return the vertex that has the value we're looking for, or None.

    Parameters
    ----------
    vertex : Vertex
        The vertex from which we're starting the DFS.

    search_val : str
        The value we're looking for during our DFS.

    visited_vertices : dict[str, bool]
        This (optional) dict helps us keep track of all the vertices 
        we've visited so far. It's initialized as an empty dict that 
        saves the value of vertex as its key and True as the value of 
        that key. Because it's passed down each function call, the key
        is added to same object in memory every time.

    Returns
    -------
    vertex : Vertex
        The vertex that has the value we're looking for.

    or

    None
    '''

    # If the value of the current vertex is the value
    # we're looking for, return that vertex:
    if vertex.value == search_val:
        return vertex

    # This is used to keep track of the visited vertices.
    # Add the vertex we pass as an argument to the dictionary,
    # because the first time we perform DFS on that vertex, it's
    # not going to be in the dict yet:
    visited_vertices[vertex.value] = True
    
    # Print all vertices we're visiting, which equals some sort
    # of visual trail we can follow whilst debugging:
    print(vertex.value)

    for adjacent_vertex in vertex.adjacent_vertices:
        if visited_vertices.get(adjacent_vertex.value):
            # If we can find the value inside our hash table,
            # we have to continue on with the next adjacent vertex,
            # because return would just end the DFS on that vertex.
            continue
        # If this adjacent vertex has the value we're looking,
        # return it:
        if adjacent_vertex.value == search_val:
            return adjacent_vertex

        # Otherwise, we have to recursively search for that value:
        vertex_with_search_val = dfs_val(
            adjacent_vertex, search_val, visited_vertices)

        # If we actually were able to find the vertex with the value
        # we're looking for return that vertex:
        if vertex_with_search_val:
            return vertex_with_search_val


alice = Vertex("Alice")
bob = Vertex("Bob")
candy = Vertex("Candy")
derek = Vertex("Derek")
elaine = Vertex("Elaine")
helen = Vertex("Helen")
fred = Vertex("Fred")
gina = Vertex("Gina")
irena = Vertex("Irena")

alice.add_adjacent_vertex(bob)
alice.add_adjacent_vertex(candy)
alice.add_adjacent_vertex(derek)
alice.add_adjacent_vertex(elaine)

bob.add_adjacent_vertex(fred)

fred.add_adjacent_vertex(helen)
fred.add_adjacent_vertex(candy)

derek.add_adjacent_vertex(gina)
derek.add_adjacent_vertex(elaine)

gina.add_adjacent_vertex(irena)

# dfs(alice)
print(dfs_val(alice, "Derek").value) # type: ignore
