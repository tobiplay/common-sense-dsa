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
        
        Keyword arguments:
        node: the node whose descendants we're collecting words from.
        word: add chars to when we're traversing the trie.
        words: a list to collect all words we're collecting. 
        '''

        pass




class TrieNode:
    def __init__(self):
        self.children = {}
