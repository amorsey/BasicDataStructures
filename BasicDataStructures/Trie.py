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


    def search(self, word):
        p = self.root
        i = 0
        length = len(word)
        while i < length and word[i] in p.children:
            p = p.children[word[i]]
            i += 1
        if i == length:
            return p


    def childWords(self, spot):
        childList = []

        if spot.endOfWord:
            childList.append("")

        for char in spot.children:
            givenList = self.childWords(spot.children[char])
            for word in givenList:
                childList.append(char+word)
        return childList


    def prefix(self, word):
        p = self.search(word)
        if p:
            l = self.childWords(p)
            newList = []
            for e in l:
                newList.append(word+e)
            return newList


    def __str__(self):
        s = ""
        l = self.childWords(self.root)
        for e in l:
            s = s + e + ","
        return s


myTrie = Trie()
myTrie.add("the")
myTrie.add("he")
myTrie.add("she")
myTrie.add("they")
myTrie.add("them")
myTrie.add("heath")
myTrie.add("see")
print(myTrie.prefix("s"))
