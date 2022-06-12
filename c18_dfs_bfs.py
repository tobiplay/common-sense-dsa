from tracemalloc import start

'''
    j <-- i <-- a --> b --> c --> h
    |           |                 |
    |           |                 |
    v           v                 v
    k --> l --> d --> e --> f --> g
'''
adjacency_list = {
    "a": ["b", "d", "i"],
    "b": ["c"],
    "c": ["h"],
    "d": ["e"],
    "e": ["f"],
    "f": ["g"],
    "g": [],
    "h": ["g"],
    "i": ["j"],
    "j": ["k"],
    "k": ["l"],
    "l": ["d"]
}


def dfs(adjacency_list: dict[str, list[str]], starting_vertex: str):
    # A stack works according to 'LIFO', last-in, first-out.
    # Add the first vertex to the list:
    stack: list[str] = [starting_vertex]
    while len(stack) > 0:
        # Pop off the vertex at the very first index:
        current_vertex = stack.pop(0)
        print(current_vertex)

        for adjacent_vertex in adjacency_list[current_vertex]:
            stack.insert(0, adjacent_vertex)


def bfs(adjacency_list: dict[str, list[str]], starting_vertex: str):
    queue: list[str] = [starting_vertex]
    # A queue works via FIFO, first-in, first-out
    while len(queue) > 0:
        current_vertex = queue.pop(0)
        print(current_vertex)
        for adjacent_vertex in adjacency_list[current_vertex]:
            queue.append(adjacent_vertex)


dfs(adjacency_list, "a")
# bfs(adjacency_list, "a")
