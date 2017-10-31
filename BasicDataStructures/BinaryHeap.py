class BinaryHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i-1)//2

    def heapUp(self, p):
        data = self.heap[p]
        pr = self.parent(p)
        while p != 0 and data > self.heap[pr]:
            self.heap[p] = self.heap[pr]
            self.heap[pr] = data
            p = pr
            pr = self.parent(p)

    def heapDown(self, p):
        data = self.heap[p]
        length = len(self.heap)
        c1 = p*2+1
        c2 = p*2+2
        if c1 < length and self.heap[c1] > data:
            self.heap[p] = self.heap[c1]
            self.heap[c1] = data
            self.heapDown(c1)
        data = self.heap[p]
        if c2 < length and self.heap[c2] > data:
            self.heap[p] = self.heap[c2]
            self.heap[c2] = data
            self.heapDown(c2)

    def insert(self, data):
        self.heap.append(data)
        position = len(self.heap)-1
        self.heapUp(position)

    def pop(self):
        length = len(self.heap)
        if length > 0:
            value = self.heap[0]
            self.heap[0] = self.heap[length-1]
            del self.heap[length-1]
            self.heapDown(0)
            return value
        return None

    def peek(self):
        return self.heap[0]

    def __str__(self):
        s = "["
        for element in self.heap:
            s += str(element)
            s += ","
        return s + "]"

myHeap = BinaryHeap()
myHeap.insert(3)
myHeap.insert(4)
myHeap.insert(9)
myHeap.insert(7)
myHeap.insert(1)
myHeap.insert(8)
myHeap.insert(6)
myHeap.insert(2)
myHeap.insert(5)
print(myHeap)
print(myHeap.pop())
print(myHeap)

