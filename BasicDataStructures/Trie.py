class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:
    def __init__(self):
        self.root = Node()

    def add(self, word):
        p = self.root
        for letter in word:
            if letter in p.children:
                p = p.children[letter]
            else:
                t = Node()
                p.children[letter] = t
                p = t
        p.endOfWord = True


    def delete(self, word):
        pass

    def search(self, word):
        p = self.root
        i = 0
        length = len(word)
        while i < length and word[i] in p.children:
            p = p.children[word[i]]
        if i == length:
            return p
        else:
            return None

    def children(self, parent, prefix):
        l = []
        for i in parent.children:
            a = children(parent.children[i])
            for e in a:
                l.append(prefix+e)
        return l


    def prefix(self, word):
        p = self.search(word)
        words = []

        if p:
            for c in p.children:
                pass


myDict = {"a": "1", "c": "2", "f": "3"}
for c in myDict:
    print(myDict[c])



myTrie = Trie()
myTrie.add("the")
myTrie.add("he")
myTrie.add("she")
myTrie.add("they")
myTrie.add("them")
myTrie.add("heath")
myTrie.add("see")


