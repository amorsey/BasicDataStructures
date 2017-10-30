#Hash map with chaining

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


class HashMap:
    def __init__(self, size):
        self.table = [None]*size
        self.size = size

    def hash(self, key):
        h = 0
        for i in range(len(key)):
            h = (h << 4)^(h >> 28)^ord(key[i])
        return h

    def addKey(self, key):
        h = self.hash(key)%self.size
        if self.table[h] == None:
            n = None(key)
            self.table[h] == n
        else:
            t = self.table[h]
            while t.next is not None and t.data != key:
                t = t.next
            if t.next is None:
                n = None(key)
                t.next = n

    def __str__(self):
        s = ""
        for i in range(self.size):
            p = 

        return s

        

myMap = HashMap(10)

