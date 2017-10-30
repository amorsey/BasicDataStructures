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
        n = Node(key)
        p = self.table[h]
        
        if p == None:
            self.table[h] = n
        else:
            while p.next != None and p.data != key:
                p = p.next
            if p.data != key:
                p.next = n

    def removeKey(self, key):
        h = self.hash(key)%self.size
        p = self.table[h]

        if p != None and p.data == key:
            self.table[h] = p.next
        elif p != None:
            while p.next != None and p.next.data != key:
                p = p.next
            if p.next.data == key:
                p.next = p.next.next

    def __str__(self):
        s = ""
        for i in range(self.size):
            s += str(i) + ":"
            p = self.table[i]
            while p != None:
                s = s + " - " + str(p.data)
                p = p.next
            s += "\n"

        return s

        

myMap = HashMap(10)
myMap.addKey("alex")
myMap.addKey("lexa")
myMap.addKey("xlea")
myMap.addKey("xael")
myMap.addKey("alex")
myMap.addKey("l")
myMap.addKey("lxea")
myMap.addKey("aexl")
myMap.addKey("xeal")
myMap.addKey("lxea")
myMap.addKey("aexl")
myMap.addKey("xeal")
myMap.removeKey("xeal")
print(myMap)

