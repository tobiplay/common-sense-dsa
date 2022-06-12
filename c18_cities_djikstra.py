class City:
    '''The City class is a vertex that helps demonstrate Djikstra's algorithm.'''

    def __init__(self, name: str):
        '''Initialize a city (vertex) with a string as its name.

        We also keep track of all possible routes. Those are edges in
        a weighted graphs network and have a certain price asigned to them.

        Parameters
        ----------
        name : str
            We asign the city a string to represent its name.

        '''
        self.name = name
        self.routes: dict[City, int] = {}

    def add_route(self, city: 'City', price: int):
        '''Add a route from this city to another city at a specifc price.

        Parameters
        ----------
        city : City
            The city to which we'd like to construct an edge, starting
            from this instance of a city.

        price : int
            The price or cost it takes to traverse from this instance of
            a city to the target city, connected via an edge.

        '''
        self.routes[city] = price


# Initialize 5 cities:
atlanta = City("Atlanta")
boston = City("Boston")
chicago = City("Chicago")
denver = City("Denver")
el_paso = City("El Paso")

# Connected the 5 cities to a weighted graph
# network with our cities:
atlanta.add_route(boston, 100)
atlanta.add_route(denver, 160)

boston.add_route(chicago, 120)
boston.add_route(denver, 180)

chicago.add_route(el_paso, 80)

denver.add_route(chicago, 40)
denver.add_route(el_paso, 140)


def dijkstra_shortest_path(starting_city: City, final_destination: City) -> list[City]:
    cheapest_prices_table: dict[str, int] = {}
    cheapest_previous_stopover_city_table: dict[str, str] = {}

    # Keep track of the cities we have not visited yet:
    unvisited_cities = []
    # Keep track of the cities we have already visited.
    # An array would be ok, but a hash table is more efficient
    # for lookups:
    visited_cities = {}

    # Add the starting city to the hash table at a
    # price of 0 (we're already here):
    cheapest_prices_table[starting_city.name] = 0

    # Make our starting city the current city:
    current_city: City = starting_city

    # Keep running as long as we can visit an unvisited city:
    while current_city:
        # Add the current city to our collection of visited cites:
        visited_cities[current_city] = True
        # Remove it from our dict that tracks the unvisited cities:
        unvisited_cities.remove(current_city)

        # Iterate over each of the adjacent cities:
        for adjacent_city, price_to_adjacent_city in current_city.routes.items():
            # If we've discovered an unknown city,
            # add it to the list of unvisited cites:
            if visited_cities.get(adjacent_city, None) == None:
                unvisited_cities.append(adjacent_city)

            # Calculate the price of getting from the starting city to the
            # adjacent city using the current city as the second-to-last stop:
            price_through_current_city = cheapest_prices_table[current_city.name] + \
                price_to_adjacent_city

            

    return [starting_city]


print(dijkstra_shortest_path(boston, atlanta))
