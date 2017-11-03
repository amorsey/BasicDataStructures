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
        pass

    def prefix(self, word):
        pass

myTrie = Trie()

s = "alex"

for l in s:
    print(l)

