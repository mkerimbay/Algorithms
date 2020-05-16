from TrieNode import TrieNode


class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node

    # Function to get the index of a character 't'
    def get_index(self, t):
        return ord(t) - ord('a')

    # Function to insert a key in the Trie
    def insert(self, key):
        if key is None:
            return

        key = key.lower()
        current_node = self.root
        index = 0

        for level in range(len(key)):
            index = self.get_index(key[level])

            if current_node.children[index] is None:
                current_node.children[index] = TrieNode(key[level])
                # print(key[level] + ' inserted')
            current_node = current_node.children[index]

        # Mark the end character as leaf node
        current_node.mark_as_leaf()
        print("'" + key + "' inserted")

    # Function to search a given key in Trie
    def search(self, word):
        if not word:
            return False

        word = word.lower()
        current_node = self.root
        index = 0

        for ch in range(len(word)):
            index = self.get_index(word[ch])
            if current_node.children[index] is None:
                return False
            current_node = current_node.children[index]

        if current_node is not None and current_node.is_end_word:
            return True

        return False

    # Function to delete given key from Trie
    def has_no_children(self, current_node):
        for i in range(len(current_node.children)):
            if current_node.children[i] is not None:
                return False
        return True

    # Recursive function to delete given key
    def delete_helper(self, key, current_node, length, level):
        deleted_self = False

        if current_node is None:
            print("Key does not exist")
            return deleted_self

        # Base Case:
        # If we have reached at the node
        # which points to the alphabet at the end of the key.
        if level is length:
            # If there are no nodes ahead of this node in this path
            # Then we can delete this node
            if self.has_no_children(current_node):
                current_node = None
                deleted_self = True

            # If there are nodes ahead of current_node in this path
            # Then we cannot delete current_node. We simply unmark this as leaf
            else:
                current_node.unMarkAsLeaf()
                deleted_self = False

        else:
            child_node = current_node.children[self.get_index(key[level])]
            child_deleted = self.delete_helper(key, child_node, length, level + 1)
            if child_deleted:
                # Making children pointer also None: since child is deleted
                current_node.children[self.get_index(key[level])] = None
                # If current_node is leaf node then
                # current_node is part of another key
                # So, we cannot delete this node and it's parent path nodes
                if current_node.is_end_word:
                    deleted_self = False

                # If child_node is deleted and current_node has more children
                # then current_node must be part of another key
                # So, we cannot delete currenNode
                elif self.has_no_children(current_node) is False:
                    deleted_self = False

                # Else we can delete current_node
                else:
                    current_node = None
                    deleted_self = True

            else:
                deleted_self = False

        return deleted_self

    def delete(self, key):
        if self.root is None or key is None:
            print('None key or empty trie error')
            return
        self.delete_helper(key, self.root, len(key), 0)

    def total_words(self, root):
        count = 0

        if root.is_end_word:
            count += 1

        for i in range(len(root.children)):
            if root.children[i] is not None:
                count += self.total_words(root.children[i])
        return count

# Input keys (use only 'a' through 'z')
keys = ["the", "a", "there", "answer", "any", "by", "bye", "their", "abc"]
output = ["Not present in trie", "Present in trie"]

t = Trie()
print("Keys to insert: ")
print(keys)

# Construct Trie
for i in range(len(keys)):
    t.insert(keys[i])


# Search for different keys
if t.search("the") is True:
    print("the --- " + output[1])
else:
    print("the --- " + output[0])

if t.search("an") is True:
    print("these --- " + output[1])
else:
    print("these --- " + output[0])

#
print(t.total_words(t.root))
