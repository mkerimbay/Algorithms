class TrieNode:
    def __init__(self, char =''):
        self.children = [None] * 26
        self.is_end_word = False
        self.char = char

    # Function to mark the current Node as Leaf
    def mark_as_leaf(self):
        self.is_end_word = True

    # Function to un-mark the current Node as Leaf
    def unmark_as_leaf(self):
        self.is_end_word = False


trie = TrieNode('a')
print(trie.char)
