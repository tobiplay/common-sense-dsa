def contains_X_orig(string: str) -> bool:
    found_X = False

    for char in string:
        if char == "X":
            found_X = True
    return found_X

def contains_X_optim(string: str) -> bool:
    for char in string:
        if char == "X":
            return True
    return False