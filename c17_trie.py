class TrieNode:
    def __init__(self):
        self.children = {}


class Trie:
    # A new trie tree is initialized with an empty TrieNode:
    def __init__(self):
        self.root: TrieNode = TrieNode()

    def search(self, string: str):
        current_node: TrieNode = self.root

        for char in string:
            if current_node.children.get(char):
                current_node = current_node.children.get(char, None)

            else:
                # If we reach this line, the word is not within the
                # trie and we exit:
                return None

        # If we reach this line, we've foudn the word.
        # Returning the current node helps with our autocomplete.
        return current_node

    def insert(self, string: str):
        current_node: TrieNode = self.root

        for char in string:
            if current_node.children.get(char):
                current_node = current_node.children[char]

            else:
                new_node = TrieNode()
                current_node.children[char] = new_node

                current_node = new_node

        # If we reach the end, add a None as a stop node.
        current_node.children["*"] = None

    def collect_all_words(self, node=None, word="", words=[]):
        '''Return all words of a specific node.

        Parameters
        ----------
        node : TrieNode
            The node whose descendants we're collecting words from.
        word : str
            The word we're adding chars to when traversing the trie.
        words : list[str] 
            A list to collect all words we're collecting. 

        Returns
        -------
        words : list[str]
            A list of all collected words.
        '''

        # Default to the root node if no node is provided.
        current_node = node or self.root

        # We iterate through all the current node's children,
        # where the key is a single char and the child_node is
        # another node (a child of the ancestor node):
        for key, child_node in current_node.children.items():
            # If the current key is *, it means we hit the end of a
            # complete word, so we can add it to our words array.
            # This is our base case:
            if key == "*":
                words.append(word)
            else:
                # If we're still in the middle of a word:
                # We recursively call this function on the child node.
                self.collect_all_words(child_node, word + key, words)

        return words

    def autocomplete(self, prefix: str) -> list[str] | None:
        '''Return all possible words that could be built with the prefix.

        Parameters
        ----------
        prefix : str
            The prefix (part of a word) we're building words from.

        Returns
        -------
        list[str] | None
            An array of words that could result from the prefix.
        '''
        # The starting node for our autocomplete is the
        # node we're passing to the function indirectly.
        # This is achieved by searching for the node by its
        # prefix:
        current_node = self.search(prefix)
        # If the node does not exist within the trie,
        # we can just return None:
        if not current_node:
            return None
        # This returns all possible extension to the prefix:
        return self.collect_all_words(current_node)

    def autocorrect(self, word: str) -> str:
        '''Return a word that stems from an autocorrected input word.

        Parameters
        ----------
        word : str
            The word the user entered and is expected to be corrected.

        Returns
        -------
        str
            A word that is thought to be the one the user was looking for.
        '''
        current_node: TrieNode = self.root
        # Keep track of how much of the word we've gathered:
        word_so_far = ""

        for char in word:
            # Check if the child of the current node has a
            # key with the char as its value:
            if current_node.children.get(char):
                # If it does we just add the char to the concat string:
                word_so_far += char
                # Now swap the current node and follow the child node:
                current_node = current_node.children.get(char, None)
            else:
                # If the current character isn't found among
                # the current node's children, collect all the suffixes that
                # descend from the current node and get the first one.
                # We concatenate the suffix with the prefix we've found so
                # far to suggest the word the user meant to type in.
                # Example: user typed in "catnafasf", we'll therefore get to
                # "catn" and collect_all_words will return ["ip",
                # "ap"].
                return word_so_far + self.collect_all_words(current_node)[0]

        # The word is found, so we just return it:
        return word

    def print_all_nodes(self, node):
        current_node = node or self.root

        for key, child_node in current_node.children.items():
            print(key)
            if key != "*":
                self.print_all_nodes(child_node)
