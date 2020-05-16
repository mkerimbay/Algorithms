class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                t[w] = {}
            t = t[w]
        t['#'] = '#' # represents end of word

    def search(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        if '#' in t:
            return True
        return False

    def prefix(self, word):
        t = self.trie
        for w in word:
            if w not in t:
                return False
            t = t[w]
        return True

    def list_words(self):
        my_list = []
        t = self.trie
        def getword(d):
            for each in d:
                my_list.append(each + getword(d[each]))
            # return list

        getword(t)
        print(my_list)


tr = Trie()
tr.insert('abc')
# tr.insert('ace')
# tr.insert('acer')
print(tr.trie)


# print(tr.search('wor'))
# print(tr.prefix('wo'))
# print('*-----')
# # print(tr.trie)
tr.list_words()

