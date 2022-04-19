def anagram(string: str) -> list[str]:
    # Assume our function is already implemented
    # and working.

    # Track all our anagrams:
    anagrams: list[str] = []

    # The problem might be "hello", where "hell"
    # could be considered our subproblem. If we
    # had all permutations of "hell" stored in
    # an array (not the final array!),
    # we would just have to access
    # each of the permutations at once and
    # insert the missing letter at each position once
    # and add that to our array.

    # For the base case we may consider that, once
    # there is only 1 letter left in the string, we
    # have to return that as an array item:
    if len(string) == 1:
        return [string[0]]

    # Our function is already working and will return
    # all correct permutations of "hell", where we cut the
    # last char:
    substring_anagrams = anagram(string[0:len(string) - 1])

    # For each anagram in our temporary array ...
    for substring_anagram in substring_anagrams:
        # we would like to add the missing char
        # once at each position. Because we are going
        # to add another char, the new length must be +1:
        for i in range(0, len(substring_anagram) + 1):
            copy_string = substring_anagram[0:i] + \
                string[-1] + substring_anagram[i:]

            anagrams.append(copy_string)

    return anagrams


print(anagram("hello"))
