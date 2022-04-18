def count_characters(list_of_strings: list[str]):
    # Let's first identify the subproblem of this problem:
    # ["c", "def", "ghij"] would be the subproblem. We would
    # just have to add the previous result to that.

    # Base case: if there's just one string left,
    # count all chars and return those.
    if len(list_of_strings) == 0:
        return 0

    # Assume our recursive function would already be working:
    first_entry = list_of_strings[0]
    return len(list_of_strings[0]) + count_characters(list_of_strings[1:])


print(count_characters(["ab", "c", "def", "ghij"]))  # -> 10
