friends = {
    "Alice": ["John", "Dirk"],
    "John": ["Alice", "Dirk", "Tim"],
    "Tim": ["John", "Dirk"],
    "Dirk": ["Alice", "John", "Tim"],
}

print(friends.get("Alice"))
