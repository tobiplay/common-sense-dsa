def anagram(string: str) -> list[str]:
    # Keep track of all possible anagrams
    collection: list[str] = []

    # To solve this problem we first have to
    # identify the subproblem: take "abcde" for
    # example. The subproblem would be "bcde".
    # -> Now assume that our function "anagram"
    # works, how we would go about this?

    # If the algorithm worked properly already,
    # we'd just take every possible variation of the
    # substring and insert the missing character
    # once at every index.

    # "hello" -> "ello" -> all mutations
    # and add h at every index of all mutations.
    # All mutations of "ello" are formed by
    # casting anagram() on "llo" and adding 
    # "e" once at every position.

    # Base case: if there's just one letter left,
    # add that to the collection.

    if len(string) == 1:
        return [string[0]]

    substring_anagrams = anagram(string[0:len(string) - 1])

    for substring_anagram in substring_anagrams:
        for i in range(0, len(substring_anagram) + 1):
            new_string = substring_anagram[0:i] + string[-1] + substring_anagram[i:]
            collection.append(new_string)

    return collection

print(anagram("abc"))